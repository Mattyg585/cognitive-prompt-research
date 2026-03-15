# Pipeline Design: Debugging Workflow

## Rationale
The original `debug` skill combines four distinct cognitive modes into a single prompt:
1. **Investigation** (Reproduce/Isolate): Divergent search for facts.
2. **Diagnosis** (Synthesise): Convergent reasoning to find root cause.
3. **Fixing** (Generation): Producing code solutions.
4. **Prevention** (Evaluation): Assessing future risks.

Mixing these modes creates interference:
* **Premature Diagnosis**: The model may form a hypothesis early and filter investigation to confirm it, missing contradictory evidence.
* **Fix Fixation**: The desire to generate code can rush the diagnosis phase.
* **Context Pollution**: The "fix" mode requires precise constraints, while "investigation" requires open exploration.

## Pipeline Architecture
We separate these modes into a three-stage pipeline:

### 1. Investigator (Divergent)
*   **Role**: Gather facts, logs, reproduction steps, and recent changes.
*   **Mode**: Investigation (Open search).
*   **Goal**: A complete picture of *what* is happening, without committing to *why*.
*   **Output**: Structured Investigation Report.

### 2. Diagnostician (Convergent)
*   **Role**: Analyze the investigation report, form hypotheses, verify against evidence.
*   **Mode**: Synthesis & Evaluation (Root cause analysis).
*   **Goal**: Identify the definitive root cause.
*   **Output**: Diagnosis & Root Cause Analysis.

### 3. Resolver (Generation)
*   **Role**: Implement the fix and prevention steps.
*   **Mode**: Generation (Code production).
*   **Goal**: A working fix and regression test.
*   **Output**: Code changes and verification plan.

## Handoffs
*   **Investigator -> Diagnostician**: Passes raw evidence and context. Filters out "guesses".
*   **Diagnostician -> Resolver**: Passes confirmed root cause and specific file locations. Filters out "dead ends".
