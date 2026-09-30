# Day 11: Valid Sudoku

- **Problem Link:** [LeetCode #36 - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
- **Difficulty:** 🟡 Medium
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-30

---

## 📝 Problem Statement

Determine if a **9 × 9 Sudoku board** is valid. Only the filled cells need to be validated according to the following rules:

1. Each **row** must contain the digits `1–9` without repetition.
2. Each **column** must contain the digits `1–9` without repetition.
3. Each of the nine **3×3 sub-boxes** must contain the digits `1–9` without repetition.

> **Note:** A partially filled board could be valid but not necessarily solvable. Only filled cells are validated.

### Example 1 — Valid:
```text
["5","3",".",".","7",".",".",".","."]
["6",".",".","1","9","5",".",".","."]
[".","9","8",".",".",".",".","6","."]
["8",".",".",".","6",".",".",".","3"]
["4",".",".","8",".","3",".",".","1"]
["7",".",".",".","2",".",".",".","6"]
[".","6",".",".",".",".","2","8","."]
[".",".",".","4","1","9",".",".","5"]
[".",".",".",".","8",".",".","7","9"]
Output: true
```

### Constraints:
- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1–9` or `'.'`

---

## 💡 Algorithm: Single-Pass Hash Sets

**Key Insight:** Map each cell `(r, c)` to its 3×3 box using:
```
box_id = (r // 3) * 3 + (c // 3)
```

This gives box indices 0–8:
```
┌───┬───┬───┐
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 4 │ 5 │
├───┼───┼───┤
│ 6 │ 7 │ 8 │
└───┴───┴───┘
```

Maintain three `defaultdict(set)` — `rows`, `cols`, `boxes` — and for each filled cell check membership in all three sets simultaneously. If any collision is found → invalid.

- **Time Complexity:** $O(1)$ — always exactly 81 cells.
- **Space Complexity:** $O(1)$ — at most 9 digits × 27 sets (all bounded constants).

---

## 💻 Python Implementation

```python
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = defaultdict(set)
        cols  = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                box_id = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True
```

---

## 🧪 Verification & Test Cases

The solution includes 7 automated unit tests covering:
1. LeetCode valid board example — `True`
2. LeetCode invalid board example — `False` (duplicate 8)
3. Completely empty board — `True` (no constraints violated)
4. Duplicate in a row — `False`
5. Duplicate in a column — `False`
6. Duplicate in a 3×3 box (different row & column) — `False`
7. Single filled cell — `True`
