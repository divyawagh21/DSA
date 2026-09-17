# DSA Streak Repository Guidelines

This repository tracks a daily Data Structures & Algorithms (DSA) progression from Beginner to Advanced, pushing daily commits to GitHub for green dot contributions.

## Automated Command: "Do todays dsa"
Whenever the user prompts "Do todays dsa":
1. Run `python scripts/dsa_runner.py next` to identify the next curriculum question.
2. Implement an optimal solution in `solutions/Day-XXX_<slug>/solution.py` with standalone unit test assertions.
3. Create `solutions/Day-XXX_<slug>/README.md` explaining the approach, trade-offs, and Big-O complexity.
4. Execute `python solutions/Day-XXX_<slug>/solution.py` to verify that all test assertions pass.
5. Execute `python scripts/dsa_runner.py complete <day_id> "solutions/Day-XXX_<slug>"` to update `data/curriculum.json` and `README.md`.
6. Execute `python scripts/dsa_runner.py push <day_id> "<title>" "<difficulty>"` to commit and push directly to GitHub.