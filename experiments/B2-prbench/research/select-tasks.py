#!/usr/bin/env python3
"""
PRBench Task Selection Script

Run this in an environment with internet access to HuggingFace.
It will select 3 tasks (easy/medium/hard) and dump their full data
as JSON files ready for the B2 experiment.

Usage:
    pip install datasets
    python select-tasks.py
"""

import json
import os
from datasets import load_dataset


def category_diversity(row):
    """Count unique rubric categories in a task."""
    cats = set()
    for c in row['rubric']:
        ann = c['annotations'] if 'annotations' in c else c
        if 'criteria_category' in ann:
            cats.add(ann['criteria_category'])
    return len(cats)


def get_weight(criterion):
    """Extract the actual weight from a criterion based on its weight_class."""
    ann = criterion.get('annotations', criterion)
    wclass = ann.get('weight_class', '')
    weight_key = wclass.replace(" ", "_") + "_weight"
    return ann.get(weight_key, 0)


def format_task(row, difficulty_label):
    """Format a task into a clean dict for export."""
    # Build conversation turns
    turns = []
    for i in range(10):
        prompt_key = f"prompt_{i}"
        response_key = f"response_{i}"
        model_key = f"model_{i}"
        ref_key = f"reference_texts_{i}"

        if prompt_key in row and row[prompt_key] and str(row[prompt_key]).strip():
            turn = {"role": "user", "content": row[prompt_key]}
            if ref_key in row and row[ref_key]:
                turn["reference_texts"] = row[ref_key]
            turns.append(turn)

        if response_key in row and row[response_key] and str(row[response_key]).strip():
            turn = {"role": "assistant", "content": row[response_key]}
            if model_key in row and row[model_key]:
                turn["model"] = row[model_key]
            turns.append(turn)

    # Build rubric
    rubric_items = []
    for c in row['rubric']:
        ann = c.get('annotations', c)
        weight = get_weight(c)
        rubric_items.append({
            "criteria_description": ann.get('criteria_description', ''),
            "criteria_category": ann.get('criteria_category', ''),
            "weight_class": ann.get('weight_class', ''),
            "weight": weight,
            "field_for_category": ann.get('field_for_category', ''),
        })

    return {
        "task_id": row['task'],
        "title": row.get('title', ''),
        "field": row['field'],
        "topic": row.get('topic', ''),
        "turns_count": row['turns'],
        "difficulty": difficulty_label,
        "conversation": turns,
        "rubric": rubric_items,
        "num_criteria": len(rubric_items),
        "num_categories": category_diversity(row),
        "scratchpad": row.get('scratchpad', ''),
    }


def print_task_summary(task_data):
    """Print a readable summary of a selected task."""
    print(f"\n{'='*80}")
    print(f"  {task_data['difficulty'].upper()}: {task_data['task_id']}")
    print(f"  Domain: {task_data['field']} | Topic: {task_data['topic']}")
    print(f"  Turns: {task_data['turns_count']} | Criteria: {task_data['num_criteria']} | Categories: {task_data['num_categories']}")
    print(f"  Title: {task_data['title']}")
    print(f"{'='*80}")

    # Show first prompt (truncated)
    first_prompt = task_data['conversation'][0]['content'] if task_data['conversation'] else 'N/A'
    print(f"\n  First prompt (first 300 chars):")
    print(f"  {first_prompt[:300]}...")

    # Show rubric categories and weights
    print(f"\n  Rubric breakdown:")
    by_cat = {}
    for r in task_data['rubric']:
        cat = r['criteria_category']
        if cat not in by_cat:
            by_cat[cat] = []
        by_cat[cat].append(r)

    for cat, items in sorted(by_cat.items()):
        weights = [i['weight'] for i in items]
        print(f"    {cat}: {len(items)} criteria, weights: {weights}")


def main():
    print("Loading PRBench dataset from HuggingFace...")

    finance = load_dataset("ScaleAI/PRBench", split="finance")
    finance_hard = load_dataset("ScaleAI/PRBench", split="finance_hard")
    legal = load_dataset("ScaleAI/PRBench", split="legal")
    legal_hard = load_dataset("ScaleAI/PRBench", split="legal_hard")

    hard_finance_ids = set(r['task'] for r in finance_hard)
    hard_legal_ids = set(r['task'] for r in legal_hard)

    print(f"Finance: {len(finance)} tasks ({len(hard_finance_ids)} hard)")
    print(f"Legal: {len(legal)} tasks ({len(hard_legal_ids)} hard)")

    # === EASY: Finance, NOT in hard, single-turn, fewer criteria ===
    easy_candidates = [r for r in finance
                       if r['task'] not in hard_finance_ids
                       and r['turns'] == 1
                       and len(r['rubric']) <= 18]
    # Sort by category diversity (more diverse = more interesting for our purposes)
    easy_candidates.sort(key=lambda r: (category_diversity(r), len(r['rubric'])), reverse=True)

    print(f"\n--- EASY candidates: {len(easy_candidates)} ---")
    for r in easy_candidates[:10]:
        print(f"  {r['task']} | {r['field']} | {r.get('topic','')} | turns={r['turns']} | criteria={len(r['rubric'])} | cats={category_diversity(r)}")

    # === MEDIUM: Legal, in hard subset, moderate criteria ===
    medium_candidates = [r for r in legal_hard
                         if 14 <= len(r['rubric']) <= 24]
    medium_candidates.sort(key=lambda r: (category_diversity(r), len(r['rubric'])), reverse=True)

    print(f"\n--- MEDIUM candidates: {len(medium_candidates)} ---")
    for r in medium_candidates[:10]:
        print(f"  {r['task']} | {r['field']} | {r.get('topic','')} | turns={r['turns']} | criteria={len(r['rubric'])} | cats={category_diversity(r)}")

    # === HARD: Either domain, hard subset, multi-turn, many criteria, many categories ===
    hard_candidates = [r for r in list(finance_hard) + list(legal_hard)
                       if r['turns'] >= 2
                       and len(r['rubric']) >= 20]
    hard_candidates.sort(key=lambda r: (category_diversity(r), len(r['rubric']), r['turns']), reverse=True)

    print(f"\n--- HARD candidates: {len(hard_candidates)} ---")
    for r in hard_candidates[:10]:
        print(f"  {r['task']} | {r['field']} | {r.get('topic','')} | turns={r['turns']} | criteria={len(r['rubric'])} | cats={category_diversity(r)}")

    # === Select one from each ===
    # Pick the first candidate from each list (highest diversity)
    # Then verify they're from different topics
    if not easy_candidates or not medium_candidates or not hard_candidates:
        print("\nERROR: Not enough candidates in one or more categories.")
        print("  Adjust the filtering criteria above.")
        return

    easy = easy_candidates[0]
    medium = medium_candidates[0]
    hard = hard_candidates[0]

    # Try to ensure different topics
    if medium.get('topic') == hard.get('topic'):
        for candidate in hard_candidates[1:]:
            if candidate.get('topic') != medium.get('topic'):
                hard = candidate
                break

    # Format and export
    tasks = {
        "easy": format_task(easy, "easy"),
        "medium": format_task(medium, "medium"),
        "hard": format_task(hard, "hard"),
    }

    for label, task_data in tasks.items():
        print_task_summary(task_data)

    # Save to files
    output_dir = os.path.dirname(os.path.abspath(__file__))
    tasks_dir = os.path.join(os.path.dirname(output_dir), "tasks")
    os.makedirs(tasks_dir, exist_ok=True)

    for label, task_data in tasks.items():
        # Save full JSON
        json_path = os.path.join(tasks_dir, f"task-{label}.json")
        with open(json_path, 'w') as f:
            json.dump(task_data, f, indent=2)
        print(f"\nSaved: {json_path}")

        # Save as readable markdown
        md_path = os.path.join(tasks_dir, f"task-{label}.md")
        with open(md_path, 'w') as f:
            f.write(f"# PRBench Task: {label.upper()}\n\n")
            f.write(f"**Task ID**: {task_data['task_id']}\n")
            f.write(f"**Title**: {task_data['title']}\n")
            f.write(f"**Domain**: {task_data['field']}\n")
            f.write(f"**Topic**: {task_data['topic']}\n")
            f.write(f"**Turns**: {task_data['turns_count']}\n")
            f.write(f"**Criteria**: {task_data['num_criteria']}\n")
            f.write(f"**Categories**: {task_data['num_categories']}\n\n")

            f.write("## Conversation\n\n")
            for turn in task_data['conversation']:
                role = turn['role'].upper()
                f.write(f"### {role}\n\n")
                if turn.get('reference_texts'):
                    f.write("**Reference texts prepended:**\n\n")
                    for rt in turn['reference_texts']:
                        f.write(f"```\n{rt}\n```\n\n")
                f.write(f"{turn['content']}\n\n")

            f.write("## Rubric\n\n")
            f.write("| # | Category | Weight Class | Weight | Criteria |\n")
            f.write("|---|----------|-------------|--------|----------|\n")
            for i, r in enumerate(task_data['rubric'], 1):
                desc = r['criteria_description'].replace('|', '\\|').replace('\n', ' ')
                f.write(f"| {i} | {r['criteria_category']} | {r['weight_class']} | {r['weight']} | {desc} |\n")

        print(f"Saved: {md_path}")

    # Save combined file
    combined_path = os.path.join(tasks_dir, "selected-tasks-all.json")
    with open(combined_path, 'w') as f:
        json.dump(tasks, f, indent=2)
    print(f"\nSaved combined: {combined_path}")

    print("\n\nDONE. Task files saved to:", tasks_dir)
    print("Next step: Copy task-easy.md, task-medium.md, task-hard.md to the experiment.")


if __name__ == "__main__":
    main()
