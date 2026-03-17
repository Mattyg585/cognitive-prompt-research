# EASY: scikit-learn__scikit-learn-10908

## Metadata

- **instance_id**: `scikit-learn__scikit-learn-10908`
- **repo**: `scikit-learn/scikit-learn`
- **difficulty**: EASY (< 15 min estimated fix time)
- **solve rate**: ~84% of agents solve scikit-learn tasks

> **NOTE**: `base_commit`, `patch`, `test_patch`, `FAIL_TO_PASS`, and `PASS_TO_PASS` must be
> retrieved from the HuggingFace dataset. See retrieval script below.

## Problem Statement

**Title**: CountVectorizer's get_feature_names raise not NotFittedError when the vocabulary parameter is provided

When instantiating a `CountVectorizer` with a custom vocabulary parameter, calling `get_feature_names()` raises `NotFittedError` despite the vocabulary being available. However, calling `transform()` works correctly because it calls `_validate_vocabulary()` internally.

### Reproduction

```python
from sklearn.feature_extraction.text import CountVectorizer

vocabulary = ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
vectorizer = CountVectorizer(vocabulary=vocabulary)

# This fails with NotFittedError -- should not
vectorizer.get_feature_names()

# But this succeeds
vectorizer.transform(["some text"])
```

### Expected Behavior

`get_feature_names()` should not raise `NotFittedError` if the vocabulary parameter was provided but the vectorizer has not been trained. The vocabulary is already known.

### Root Cause

`get_feature_names()` checks for `vocabulary_` (the fitted attribute) but does not call `_validate_vocabulary()` which would copy the user-provided `vocabulary` parameter into `vocabulary_`.

### Fix

Add a call to `_validate_vocabulary()` in `get_feature_names()` before accessing `self.vocabulary_`.

## Links

- **GitHub Issue**: https://github.com/scikit-learn/scikit-learn/issues/10901
- **GitHub PR**: https://github.com/scikit-learn/scikit-learn/pull/10908

## Why This Is Easy

1. Single file change (likely `sklearn/feature_extraction/text.py`)
2. The fix pattern already exists in `transform()` -- just replicate it
3. Clear reproduction steps in the issue
4. Simple validation logic, no algorithmic complexity
5. scikit-learn tasks have the highest per-repo solve rate in SWE-bench Verified

## Data Retrieval

```python
from datasets import load_dataset
ds = load_dataset('princeton-nlp/SWE-bench_Verified', split='test')
task = [x for x in ds if x['instance_id'] == 'scikit-learn__scikit-learn-10908'][0]
print(f"base_commit: {task['base_commit']}")
print(f"version: {task['version']}")
print(f"patch:\n{task['patch']}")
print(f"test_patch:\n{task['test_patch']}")
print(f"FAIL_TO_PASS: {task['FAIL_TO_PASS']}")
```
