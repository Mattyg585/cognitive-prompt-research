#!/usr/bin/env python3
"""
Score B2-PRBench outputs against rubric criteria.

Reads each output file, scores each criterion using the PRBench judge template,
and produces a results JSON with per-criterion and aggregate scores.

Usage:
    python3 score.py

Requires ANTHROPIC_API_KEY environment variable.
"""

import json
import os
import sys
import anthropic

BASE = os.path.dirname(os.path.abspath(__file__))

# PRBench judge template (from constants.py)
GRADER_TEMPLATE = """Your job is to look at a response and a rubric item, and score the response on how well it follows the rubric item.

# Response
{response}

# Rubric item
{rubric_item}

# Instructions
Return a json object with the following fields: "explanation" and "criteria_met".
- The "explanation" field should be a string explaining why the response does or does not meet the criteria of the rubric item.
- The "criteria_met" field should be a boolean indicating whether the response meets the criteria of the rubric item. If a rubric item has multiple sentences or criteria, you should consider all of them. If any of the criteria is not met, the answer should be false. Only return true if all of the criteria are met.
- One important exception: if a criteria says "such as", "for example", or "including", the response does not have to include all of the examples listed to meet the criteria.

Return just the json object in markdown format. Do not include any other text."""


def load_task(difficulty):
    """Load task data from JSON."""
    with open(os.path.join(BASE, "tasks", f"task-{difficulty}.json")) as f:
        return json.load(f)


def load_response(tier, difficulty):
    """Load a response file."""
    paths = {
        ("baseline", "easy"): "baseline-runs/baseline-easy.md",
        ("baseline", "hard"): "baseline-runs/baseline-hard.md",
        ("tier2", "easy"): "optimised-runs/tier2-easy.md",
        ("tier2", "hard"): "optimised-runs/tier2-hard.md",
        ("pipeline", "easy"): "pipeline-runs/pipeline-easy.md",
        ("pipeline", "hard"): "pipeline-runs/pipeline-hard.md",
    }
    path = os.path.join(BASE, paths[(tier, difficulty)])
    with open(path) as f:
        return f.read()


def score_criterion(client, response_text, criterion_desc):
    """Score a single criterion against a response using Sonnet."""
    prompt = GRADER_TEMPLATE.format(
        response=response_text,
        rubric_item=criterion_desc,
    )

    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    # Parse the response
    text = msg.content[0].text
    # Extract JSON from markdown code block if present
    if "```json" in text:
        text = text.split("```json")[1].split("```")[0].strip()
    elif "```" in text:
        text = text.split("```")[1].split("```")[0].strip()

    try:
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        print(f"  WARNING: Could not parse judge response: {text[:200]}")
        return {"explanation": text, "criteria_met": False}


def calculate_score(criteria_results):
    """Calculate PRBench clipped score."""
    total_points = 0
    total_positive_weights = 0

    for r in criteria_results:
        weight = r["weight"]
        met = 1 if r["criteria_met"] else 0
        total_points += met * weight
        if weight > 0:
            total_positive_weights += weight

    if total_positive_weights == 0:
        return 0

    score = total_points / total_positive_weights
    return max(0, min(1, score))  # clip to [0, 1]


def score_by_category(criteria_results):
    """Calculate scores per rubric category."""
    categories = {}
    for r in criteria_results:
        cat = r["criteria_category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)

    cat_scores = {}
    for cat, items in categories.items():
        total = sum(r["weight"] for r in items if r["weight"] > 0)
        earned = sum(r["weight"] for r in items if r["criteria_met"] and r["weight"] > 0)
        cat_scores[cat] = earned / total if total > 0 else 0

    return cat_scores


def main():
    client = anthropic.Anthropic()

    results = {}

    for difficulty in ["easy", "hard"]:
        task = load_task(difficulty)
        rubric = task["rubric"]

        for tier in ["baseline", "tier2", "pipeline"]:
            key = f"{tier}-{difficulty}"
            print(f"\n{'='*60}")
            print(f"Scoring: {key} ({len(rubric)} criteria)")
            print(f"{'='*60}")

            response = load_response(tier, difficulty)
            criteria_results = []

            for i, criterion in enumerate(rubric):
                desc = criterion["criteria_description"]
                cat = criterion["criteria_category"]
                weight = criterion["weight"]
                weight_class = criterion["weight_class"]

                print(f"  [{i+1}/{len(rubric)}] {cat} (w={weight}): {desc[:60]}...", end=" ", flush=True)

                result = score_criterion(client, response, desc)
                met = result.get("criteria_met", False)
                print("MET" if met else "NOT MET")

                criteria_results.append({
                    "criterion_index": i + 1,
                    "criteria_description": desc,
                    "criteria_category": cat,
                    "weight": weight,
                    "weight_class": weight_class,
                    "criteria_met": met,
                    "explanation": result.get("explanation", ""),
                })

            overall = calculate_score(criteria_results)
            by_category = score_by_category(criteria_results)

            results[key] = {
                "tier": tier,
                "difficulty": difficulty,
                "overall_score": round(overall, 4),
                "category_scores": {k: round(v, 4) for k, v in by_category.items()},
                "criteria_results": criteria_results,
                "criteria_met_count": sum(1 for r in criteria_results if r["criteria_met"]),
                "criteria_total": len(criteria_results),
            }

            print(f"\n  SCORE: {overall:.4f} ({sum(1 for r in criteria_results if r['criteria_met'])}/{len(criteria_results)} criteria met)")
            for cat, score in sorted(by_category.items()):
                print(f"    {cat}: {score:.4f}")

    # Save results
    output_path = os.path.join(BASE, "evaluation", "scores.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Print comparison table
    print(f"\n{'='*60}")
    print("COMPARISON")
    print(f"{'='*60}")

    for difficulty in ["easy", "hard"]:
        print(f"\n--- {difficulty.upper()} TASK ---")
        print(f"{'Tier':<12} {'Score':<8} {'Met':<6}")
        for tier in ["baseline", "tier2", "pipeline"]:
            key = f"{tier}-{difficulty}"
            r = results[key]
            print(f"{tier:<12} {r['overall_score']:<8.4f} {r['criteria_met_count']}/{r['criteria_total']}")

        # Category comparison
        all_cats = set()
        for tier in ["baseline", "tier2", "pipeline"]:
            all_cats.update(results[f"{tier}-{difficulty}"]["category_scores"].keys())

        print(f"\n{'Category':<35} {'Baseline':<10} {'Tier2':<10} {'Pipeline':<10}")
        for cat in sorted(all_cats):
            scores = []
            for tier in ["baseline", "tier2", "pipeline"]:
                s = results[f"{tier}-{difficulty}"]["category_scores"].get(cat, 0)
                scores.append(f"{s:.4f}")
            print(f"{cat:<35} {scores[0]:<10} {scores[1]:<10} {scores[2]:<10}")


if __name__ == "__main__":
    main()
