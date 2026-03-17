# B1 Baseline: Anthropic SWE-bench Scaffold Prompt

This is the prompt used by Anthropic's SWE-bench scaffold — the most minimal of the major scaffolds.
The model receives this plus two tools (Bash, Edit). That's it.

Source: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/swe-bench-sonnet)

---

## Instance Template (sent as user message)

```
<uploaded_files>/repo</uploaded_files>
I've uploaded a python code repository in the directory /repo.
Consider the following PR description:

<pr_description>{problem_statement}</pr_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <pr_description> are met?
I've already taken care of all changes to any of the test files described in the <pr_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!

Your task is to make the minimal changes to non-tests files in the /repo directory to ensure the <pr_description> is satisfied.

Follow these steps to resolve the issue:
1. Explore the repo to familiarize yourself with its structure.
2. Create a script to reproduce the error and execute it with python
3. Edit the sourcecode of the repo to resolve the issue
4. Rerun your reproduce script and confirm that the error is fixed!
5. Think about edgecases and make sure your fix handles them as well
```

## Design Philosophy

From the Anthropic blog: "Our design philosophy was to give as much control as possible to the language model itself, and keep the scaffolding minimal."

- Two tools only: Bash + Edit (string replacement)
- No elaborate workflow instructions
- Model decides its own strategy

## For Our Experiment

When running in Claude Code, this translates to:
- No CLAUDE.md file
- Paste the problem statement directly as the user message
- Let Claude Code use its default tools and behavior

The 5-step workflow in the instance template is the monolithic prompt we're testing against.
