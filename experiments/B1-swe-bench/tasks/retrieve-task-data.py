#!/usr/bin/env python3
"""
Retrieve full task data from HuggingFace SWE-bench Verified dataset.

Run this script from a machine with internet access to HuggingFace:
    pip install datasets
    python retrieve-task-data.py

It will print all fields for the three selected tasks and save them to JSON.
"""

import json
from datasets import load_dataset

TARGET_IDS = [
    'scikit-learn__scikit-learn-10908',
    'django__django-11964',
    'sympy__sympy-23413',
]

def main():
    print("Loading SWE-bench Verified dataset...")
    ds = load_dataset('princeton-nlp/SWE-bench_Verified', split='test')

    tasks = {}
    for item in ds:
        if item['instance_id'] in TARGET_IDS:
            tasks[item['instance_id']] = dict(item)

    # Verify all found
    for tid in TARGET_IDS:
        if tid not in tasks:
            print(f"WARNING: {tid} not found in dataset!")
        else:
            print(f"\nFound: {tid}")
            t = tasks[tid]
            print(f"  repo: {t['repo']}")
            print(f"  base_commit: {t['base_commit']}")
            print(f"  version: {t['version']}")
            print(f"  difficulty: {t.get('difficulty', 'N/A')}")
            print(f"  FAIL_TO_PASS: {t['FAIL_TO_PASS']}")
            print(f"  patch length: {len(t['patch'])} chars")
            print(f"  test_patch length: {len(t['test_patch'])} chars")
            print(f"  problem_statement length: {len(t['problem_statement'])} chars")

    # Save full data
    output_file = 'task-data.json'
    with open(output_file, 'w') as f:
        json.dump(tasks, f, indent=2, default=str)
    print(f"\nFull task data saved to {output_file}")

    # Also save individual files
    for tid, t in tasks.items():
        slug = tid.replace('/', '_').replace('__', '-')

        # Save problem statement
        with open(f'{slug}-problem.txt', 'w') as f:
            f.write(t['problem_statement'])

        # Save gold patch
        with open(f'{slug}-gold-patch.diff', 'w') as f:
            f.write(t['patch'])

        # Save test patch
        with open(f'{slug}-test-patch.diff', 'w') as f:
            f.write(t['test_patch'])

        print(f"Saved individual files for {tid}")

if __name__ == '__main__':
    main()
