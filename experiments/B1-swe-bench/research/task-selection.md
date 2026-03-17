# SWE-bench Verified Task Selection

## Dataset Overview

**Source**: `princeton-nlp/SWE-bench_Verified` on HuggingFace (also mirrored at `SWE-bench/SWE-bench_Verified`)
**Size**: 500 instances, ~2.1MB Parquet
**Split**: `test` only

### Dataset Schema

Each instance contains:

```python
{
    "instance_id": "owner__repo-pr_number",       # e.g. "django__django-11964"
    "repo": "owner/repo",                          # e.g. "django/django"
    "issue_id": int,                               # GitHub issue number
    "base_commit": "commit_hash",                  # Commit to check out before applying patch
    "problem_statement": "Issue description...",    # Full GitHub issue text (title + body)
    "version": "package_version",                  # Repo version at the time
    "issue_url": "GitHub issue URL",
    "pr_url": "GitHub pull request URL",
    "patch": "gold_solution_patch",                # The human-written fix (diff format)
    "test_patch": "test_patch",                    # Tests that verify the fix (diff format)
    "created_at": "date",
    "FAIL_TO_PASS": "json_list_of_test_names",     # Tests that should pass after fix
    "PASS_TO_PASS": "json_list_of_test_names",     # Tests that should still pass
    "difficulty": "difficulty_level"                # Human-annotated difficulty
}
```

### Repository Distribution in Verified

| Repository | Count | % |
|---|---|---|
| django/django | 231 | 46.2% |
| sympy/sympy | 75 | 15.0% |
| sphinx-doc/sphinx | 44 | 8.8% |
| matplotlib/matplotlib | 34 | 6.8% |
| scikit-learn/scikit-learn | 32 | 6.4% |
| pydata/xarray | 22 | 4.4% |
| astropy/astropy | 22 | 4.4% |
| pytest-dev/pytest | 19 | 3.8% |
| pylint-dev/pylint | 10 | 2.0% |
| psf/requests | 8 | 1.6% |
| mwaskom/seaborn | 2 | 0.4% |
| pallets/flask | 1 | 0.2% |

### Difficulty Distribution (Human-Annotated Time Estimates)

- **< 15 minutes** (easy): 196 instances (39.2%)
- **15 min - 1 hour** (medium): ~259 instances (~51.8%)
- **1 - 4 hours** (hard): ~42 instances (~8.4%)
- **> 4 hours** (very hard): ~3 instances (0.6%)

91% of issues estimated to take < 1 hour for an experienced human.

### Current SOTA Solve Rates (as of March 2026)

| Model/System | Verified Score |
|---|---|
| Claude Opus 4.6 (Thinking) | 79.2% |
| GPT 5.4 | 77.2% |
| Gemini 3 Flash | 76.2% |
| Claude Opus 4.5 | 80.9% (self-reported) |

Per-repository typical solve rates (from GLM-4.7 at 68.2% overall):
- scikit-learn: **84.4%** (27/32) - easiest repo
- pytest: 78.9% (15/19)
- xarray: 72.7% (16/22)
- django: 70.6% (163/231)
- matplotlib: 70.6% (24/34)
- sympy: **65.3%** (49/75) - harder repo
- sphinx: 59.1% (26/44)
- astropy: 54.5% (12/22)
- requests: 50.0% (4/8)
- pylint: **30.0%** (3/10) - hardest repo

---

## Selected Tasks

### EASY: `scikit-learn__scikit-learn-10908`

**Repo**: scikit-learn/scikit-learn
**Why easy**:
- scikit-learn has the highest per-repo solve rate (~84%)
- Single-file fix with clear validation logic
- The issue is well-specified with exact reproduction steps
- The fix involves adding a validation call to `get_feature_names()`
- Estimated fix time: < 15 minutes
- The solution is essentially: call `_validate_vocabulary()` before accessing vocabulary in `get_feature_names()`

**Problem**: `CountVectorizer.get_feature_names()` raises `NotFittedError` when a vocabulary parameter was provided at init time but `fit()` was never called. However, `transform()` works correctly in this case because it calls `_validate_vocabulary()` internally. The fix is to add the same validation to `get_feature_names()`.

**GitHub Issue**: https://github.com/scikit-learn/scikit-learn/issues/10901
**GitHub PR**: https://github.com/scikit-learn/scikit-learn/pull/10908

### MEDIUM: `django__django-11964`

**Repo**: django/django
**Why medium**:
- Django has a moderate solve rate (~71%)
- Requires understanding Django's enum system (TextChoices/IntegerChoices)
- The fix involves adding a `__str__()` method to a base class
- Multiple possible implementation approaches were debated (7 options)
- Estimated fix time: 15-60 minutes
- Requires understanding of how Django enums interact with database field retrieval

**Problem**: When you create an instance of a model with a `CharField` using `TextChoices` or `IntegerField` using `IntegerChoices`, the value returned by the getter is of the enum type, not the primitive type. Calling `str()` on it gives `MyEnum.MyValue` instead of `my_value`. This creates inconsistency between freshly-created and database-retrieved instances, and breaks external API communication.

**Django Ticket**: https://code.djangoproject.com/ticket/30902
**GitHub PR**: https://github.com/django/django/pull/11964

### HARD: `sympy__sympy-23413`

**Repo**: sympy/sympy
**Why hard**:
- sympy has a lower solve rate (~65%)
- Requires understanding the Hermite Normal Form algorithm (Cohen93 Algorithm 2.4.5)
- The bug is in a mathematical algorithm's halting condition
- Multi-file or conceptually deep fix: the algorithm exits after examining n rows rather than after finding n pivots
- Agents commonly give up or incorrectly declare the math is wrong
- Only solvable by understanding the mathematical invariant being violated
- Estimated fix time: 1-4 hours

**Problem**: `hermite_normal_form()` incorrectly removes rows from m x n matrices where n < m. The algorithm's early halting condition checks whether enough rows have been examined instead of whether enough independent pivots have been found, causing valid rows to be discarded.

Example: Applying HNF to `[[5, 8, 12], [0, 0, 1]]` (via transpose/flip workaround for row-style HNF) should give `[[5, 8, 0], [0, 0, 1]]` but instead gives `[[5, 8, 0]]` -- a row is lost.

**GitHub Issue**: https://github.com/sympy/sympy/issues/23410
**GitHub PR**: https://github.com/sympy/sympy/pull/23413

---

## Data Retrieval

The HuggingFace API and datasets library are blocked from this environment. To retrieve the full task data (base_commit, patch, test_patch, FAIL_TO_PASS, etc.), run locally:

```python
from datasets import load_dataset

ds = load_dataset('princeton-nlp/SWE-bench_Verified', split='test')

target_ids = [
    'scikit-learn__scikit-learn-10908',
    'django__django-11964',
    'sympy__sympy-23413',
]

for item in ds:
    if item['instance_id'] in target_ids:
        print(f"\n{'='*80}")
        print(f"instance_id: {item['instance_id']}")
        print(f"repo: {item['repo']}")
        print(f"base_commit: {item['base_commit']}")
        print(f"version: {item['version']}")
        print(f"difficulty: {item['difficulty']}")
        print(f"\nproblem_statement:\n{item['problem_statement']}")
        print(f"\npatch:\n{item['patch']}")
        print(f"\ntest_patch:\n{item['test_patch']}")
        print(f"\nFAIL_TO_PASS: {item['FAIL_TO_PASS']}")
        print(f"\nPASS_TO_PASS: {item['PASS_TO_PASS']}")
```

Or download the Parquet file directly:
```bash
# From the HuggingFace datasets server
wget "https://huggingface.co/datasets/princeton-nlp/SWE-bench_Verified/resolve/main/data/test-00000-of-00001.parquet"
python -c "import pandas as pd; df = pd.read_parquet('test-00000-of-00001.parquet'); print(df[df.instance_id.isin(['scikit-learn__scikit-learn-10908','django__django-11964','sympy__sympy-23413'])].to_json(orient='records', indent=2))"
```

---

## Contamination & Validity Notes

OpenAI has stopped evaluating on SWE-bench Verified (as of 2026), citing:
1. **Training data contamination**: frontier models can reproduce verbatim gold patches for some tasks
2. **Flawed hard tasks**: 59.4% of the 138 hardest (unsolved by o3 over 64 runs) had material issues in test design or problem description
3. **Benchmark saturation**: scores have stalled at ~80% for 6 months

For our experiment this is fine -- we are testing prompt optimization, not measuring absolute model capability. Contamination affects all three tiers equally, so relative comparisons remain valid. We specifically avoid tasks known to be contaminated (like `django__django-11099` which OpenAI flagged as having verbatim solutions in training data).
