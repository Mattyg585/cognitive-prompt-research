# HARD: sympy__sympy-23413

## Metadata

- **instance_id**: `sympy__sympy-23413`
- **repo**: `sympy/sympy`
- **difficulty**: HARD (1-4 hours estimated fix time)
- **solve rate**: ~65% of agents solve sympy tasks; this specific task requires mathematical understanding

> **NOTE**: `base_commit`, `patch`, `test_patch`, `FAIL_TO_PASS`, and `PASS_TO_PASS` must be
> retrieved from the HuggingFace dataset. See retrieval script below.

## Problem Statement

**Title**: Bug with HNF removing rows

The `hermite_normal_form()` function incorrectly removes rows from m x n matrices where n < m (more rows than columns).

### Reproduction

```python
import numpy as np
from sympy import Matrix
from sympy.polys.matrices.normalforms import hermite_normal_form

# Try to compute row-style HNF via transpose/flip workaround
M = Matrix(np.flip(np.array([[5, 8, 12], [0, 0, 1]])).T)
result = hermite_normal_form(M)
row_hnf = np.flip(np.array(result.T))

# Expected: [[5, 8, 0], [0, 0, 1]]
# Actual:   [[5, 8, 0]]  <-- second row is LOST
```

The function falsely identifies the matrix as rank-deficient and removes a row.

### Root Cause

The bug is in the implementation of Algorithm 2.4.5 from Cohen's "A Course in Computational Algebraic Number Theory" (1993). The algorithm's halting condition is incorrect:

- **What it does**: Terminates after examining n rows
- **What it should do**: Terminate after finding n pivots

When a pivot isn't found in an intermediate row, the algorithm exits prematurely because it has examined enough rows, even though it hasn't found all the pivots it needs. This causes valid rows to be discarded in "tall" matrices (m x n where n < m).

### Fix Location

`sympy/polys/matrices/normalforms.py` -- specifically the `_hermite_normal_form()` function's loop condition and/or the early termination logic.

The fix repairs the halting condition so the algorithm continues processing rows until all necessary pivots are identified, rather than stopping after examining a fixed number of rows.

## Links

- **GitHub Issue**: https://github.com/sympy/sympy/issues/23410
- **GitHub PR**: https://github.com/sympy/sympy/pull/23413
- **Related Issue**: https://github.com/sympy/sympy/issues/23260 (HNF works in a strange way)

## Why This Is Hard

1. **Mathematical knowledge required**: Understanding Hermite Normal Form and the Cohen93 algorithm
2. **Subtle algorithmic bug**: The error is in a loop termination condition, not a typo or missing validation
3. **Agents give up**: Commonly, agents incorrectly declare the user's mathematical expectations are wrong rather than finding the bug
4. **Requires reading the reference algorithm**: Must understand what "examining rows" vs "finding pivots" means in context
5. **Edge case**: Only manifests for specific matrix dimensions (n < m)
6. **sympy has lower solve rate**: ~65% overall, and math-heavy tasks are the hardest within sympy
7. **Conceptual depth**: The fix requires understanding an invariant (pivot count) that the original code violates

## Data Retrieval

```python
from datasets import load_dataset
ds = load_dataset('princeton-nlp/SWE-bench_Verified', split='test')
task = [x for x in ds if x['instance_id'] == 'sympy__sympy-23413'][0]
print(f"base_commit: {task['base_commit']}")
print(f"version: {task['version']}")
print(f"patch:\n{task['patch']}")
print(f"test_patch:\n{task['test_patch']}")
print(f"FAIL_TO_PASS: {task['FAIL_TO_PASS']}")
```
