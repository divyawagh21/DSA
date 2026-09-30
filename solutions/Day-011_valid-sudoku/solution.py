"""
LeetCode #36: Valid Sudoku
Difficulty: Medium
Topic: Arrays & Hashing
Date Solved: 2026-09-30

Problem:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9
   without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated.
"""

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validate the Sudoku board in a single O(81) = O(1) pass using hash sets.

        Intuition:
        We need to check three constraints simultaneously:
        - No digit repeats in any row.
        - No digit repeats in any column.
        - No digit repeats in any 3x3 sub-box.

        We maintain three collections of sets:
        - rows[r]   — digits seen in row r
        - cols[c]   — digits seen in column c
        - boxes[b]  — digits seen in 3x3 box b

        The key insight for mapping (r, c) to a box index:
            box_id = (r // 3) * 3 + (c // 3)
        This maps the 9 boxes to indices 0–8:
            (0,0)→0  (0,1)→1  (0,2)→2
            (1,0)→3  (1,1)→4  (1,2)→5
            (2,0)→6  (2,1)→7  (2,2)→8

        For every filled cell (r, c) with digit d:
        - If d is already in rows[r], cols[c], OR boxes[box_id] → invalid.
        - Otherwise, add d to all three sets and continue.

        Complexity:
        - Time Complexity: O(1) — the board is always exactly 9x9 = 81 cells.
          We process each cell exactly once.
        - Space Complexity: O(1) — at most 9 digits × 27 sets, all bounded
          constants regardless of input size.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue  # Skip empty cells

                box_id = (r // 3) * 3 + (c // 3)

                # Check all three constraints
                if (val in rows[r] or
                        val in cols[c] or
                        val in boxes[box_id]):
                    return False

                # Mark the digit as seen in this row, column, and box
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_id].add(val)

        return True


# --- Unit Tests ---
def test_is_valid_sudoku():
    solver = Solution()

    # Test Case 1: LeetCode Example — valid board
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solver.isValidSudoku(valid_board) is True, "TC1 failed"

    # Test Case 2: LeetCode Example — invalid board (duplicate 8 in top-left box)
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solver.isValidSudoku(invalid_board) is False, "TC2 failed"

    # Test Case 3: Completely empty board — valid (no violations)
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert solver.isValidSudoku(empty_board) is True, "TC3 failed"

    # Test Case 4: Duplicate in a row
    row_dup = [["." for _ in range(9)] for _ in range(9)]
    row_dup[0][0] = "5"
    row_dup[0][5] = "5"  # Duplicate 5 in row 0
    assert solver.isValidSudoku(row_dup) is False, "TC4 failed"

    # Test Case 5: Duplicate in a column
    col_dup = [["." for _ in range(9)] for _ in range(9)]
    col_dup[0][0] = "3"
    col_dup[5][0] = "3"  # Duplicate 3 in column 0
    assert solver.isValidSudoku(col_dup) is False, "TC5 failed"

    # Test Case 6: Duplicate in a 3x3 box (but not in same row/col)
    box_dup = [["." for _ in range(9)] for _ in range(9)]
    box_dup[0][0] = "7"
    box_dup[1][1] = "7"  # Both in box 0, different row and col
    assert solver.isValidSudoku(box_dup) is False, "TC6 failed"

    # Test Case 7: Single filled cell — always valid
    single = [["." for _ in range(9)] for _ in range(9)]
    single[4][4] = "5"
    assert solver.isValidSudoku(single) is True, "TC7 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_is_valid_sudoku()
