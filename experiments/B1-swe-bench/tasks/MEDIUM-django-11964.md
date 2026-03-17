# MEDIUM: django__django-11964

## Metadata

- **instance_id**: `django__django-11964`
- **repo**: `django/django`
- **difficulty**: MEDIUM (15 min - 1 hour estimated fix time)
- **solve rate**: ~71% of agents solve django tasks

> **NOTE**: `base_commit`, `patch`, `test_patch`, `FAIL_TO_PASS`, and `PASS_TO_PASS` must be
> retrieved from the HuggingFace dataset. See retrieval script below.

## Problem Statement

**Title**: The value of a TextChoices/IntegerChoices field has a differing type

**Django Ticket**: #30902

If you create an instance of a model having a CharField or IntegerField with choices pointing to IntegerChoices or TextChoices, the value returned by the getter will be of the enum type, not the expected primitive type.

When invoking `__str__(...)` you don't actually get the value property of the enum value. This leads to:

1. Inconsistency between freshly-created instances and database-retrieved instances
2. `str(instance.field)` returns `MyEnum.MyValue` instead of `my_value`
3. External API communication breaks: a fresh instance sends `MyEnum.MyValue` while a retrieved instance sends `my_value`

### The Core Issue

```python
from django.db import models

class MyChoices(models.TextChoices):
    FIRST = 'first', 'First Choice'
    SECOND = 'second', 'Second Choice'

class MyModel(models.Model):
    choice = models.CharField(max_length=10, choices=MyChoices.choices)

# After creating:
obj = MyModel(choice=MyChoices.FIRST)
str(obj.choice)  # Returns "MyChoices.FIRST" -- WRONG
# Expected: "first"

# After retrieving from DB:
obj = MyModel.objects.get(pk=1)
str(obj.choice)  # Returns "first" -- correct
```

### Solution Discussion

Seven options were debated on the ticket. The accepted solution was **option 4**: implement `__str__()` on the base `Choices` class to return `str(self.value)`.

This deliberately deviates from standard Python enum `__str__` behavior because Django's Choices are designed for database field values, not general-purpose enums.

### Fix

Add a `__str__()` method to Django's `Choices` base class (or `TextChoices`/`IntegerChoices` specifically) that returns `str(self.value)` instead of the default enum `__str__` representation.

## Links

- **Django Ticket**: https://code.djangoproject.com/ticket/30902
- **GitHub PR**: https://github.com/django/django/pull/11964

## Why This Is Medium

1. The fix itself is small (add `__str__` method)
2. BUT: requires understanding Django's enum choices system
3. Multiple valid implementation approaches (7 discussed)
4. Need to understand the difference between `Choices`, `TextChoices`, and `IntegerChoices`
5. Need to place the fix at the right level in the class hierarchy
6. The deviation from standard enum behavior must be intentional
7. Django has a moderate solve rate (~71%)

## Data Retrieval

```python
from datasets import load_dataset
ds = load_dataset('princeton-nlp/SWE-bench_Verified', split='test')
task = [x for x in ds if x['instance_id'] == 'django__django-11964'][0]
print(f"base_commit: {task['base_commit']}")
print(f"version: {task['version']}")
print(f"patch:\n{task['patch']}")
print(f"test_patch:\n{task['test_patch']}")
print(f"FAIL_TO_PASS: {task['FAIL_TO_PASS']}")
```
