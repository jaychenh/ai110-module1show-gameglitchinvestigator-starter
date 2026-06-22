# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Use the AI agent to update project documentation, summarize the final commit message, and record the agent workflow in `ai_interactions.md`.

**What did the agent do?**

- Reviewed the project files in the repository, especially `README.md`, `app.py`, `logic_utils.py`, and `tests/test_game_logic.py`.
- Updated the AI interaction log with a clear description of the agent workflow.
- Confirmed the final commit message format and provided a concise summary.

**What did you have to verify or fix manually?**

- Verified the accuracy of the log entries and ensured the descriptions matched the actual changes made.
- Confirmed the final commit message wording was appropriate for the updated documentation.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
The bug was in app.py around Submit Guess 🚀
The code was counting an attempt on every button click, even when the input was empty or invalid
That caused Attempts left: to decrease incorrectly and could go negative
The correct fix is to only increment st.session_state.attempts after parse_guess(raw_guess) succeeds and a valid guess is processed
Agent Workflow: task was to update docs, summarize commit message, and log the workflow.
Linting & Style: prompt described a bug in app.py where attempts were counted incorrectly.
Test Generation and Model Comparison sections are present but not filled in yet.
Asked how to run the test file.
Reported error: file or directory not found: tests/test_game_logic.py.
Clarified that the command was run from inside tests, and the correct path should be relative to the current directory.
Reported a pytest collection error when running from project root.
I diagnosed the failure as ImportError: attempted relative import beyond top-level package.
I fixed test_game_logic.py to use from logic_utils import check_guess and verified
Reported a bug: “the new game does not reset the game properly”
Asked why the hint system keeps changing from “Too High” to “Too Low” for the same guess
Requested a summary of the prompts themselves
Refactor core game logic from app.py into logic_utils.py
Fix the check_guess function
Correct difficulty ranges so Hard is harder than Normal
Update UI attempt limits to:
Easy: 5
Normal: 6
Hard: 8
Create/adjust pytest coverage in test_game_logic.py
Connect test_game_logic.py to logic_utils
Diagnose the ImportError: attempted relative import with no known parent package
That’s the set of prompts you’ve given so far.
Update project documentation and log the agent workflow in ai_interactions.md
Summarize the final commit message
Fix a bug in app.py around the submit/guess flow
Diagnose and fix test issues, including an import error in test_game_logic.py
Refactor core game logic from app.py into logic_utils.py
Fix check_guess() behavior
Correct difficulty ranges so Hard is harder than Normal
Update attempt limits for each difficulty
Add or adjust pytest coverage for game logic
Connect test_game_logic.py to logic_utils.py
Fix the range display so the UI shows the correct low/high values
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
