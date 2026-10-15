"""
LeetCode #22: Generate Parentheses
Difficulty: Medium
Topic: Stack
Date Solved: 2026-10-15

Problem:
Given `n` pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all valid combinations of n pairs of parentheses using
        Backtracking with an explicit Stack.

        Intuition:
        To form well-formed parentheses of length 2n:
        1. We can only add an open bracket '(' if `open_count < n`.
        2. We can only add a close bracket ')' if `close_count < open_count`
           (we cannot close brackets that haven't been opened yet).
        3. A valid combination is complete when `open_count == close_count == n`.

        By pruning invalid branches early, we only explore paths guaranteed to
        produce valid well-formed parentheses without needing to generate all 2^(2n)
        strings and validate afterwards.

        Complexity:
        - Time Complexity: O(4^n / sqrt(n)) — Bounded by the n-th Catalan number:
          C_n = (1 / (n + 1)) * comb(2n, n).
        - Space Complexity: O(n) — The stack and recursion depth are bounded by 2n.
        """
        stack = []
        result = []

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result


# --- Unit Tests ---
def test_generate_parenthesis():
    solver = Solution()

    # Test Case 1: n = 1 -> 1 combination (C_1 = 1)
    assert solver.generateParenthesis(1) == ["()"], "TC1 failed on n=1"

    # Test Case 2: n = 2 -> 2 combinations (C_2 = 2)
    expected2 = sorted(["(())", "()()"])
    assert sorted(solver.generateParenthesis(2)) == expected2, "TC2 failed on n=2"

    # Test Case 3: n = 3 -> 5 combinations (C_3 = 5, LeetCode example)
    expected3 = sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert sorted(solver.generateParenthesis(3)) == expected3, "TC3 failed on n=3"

    # Test Case 4: n = 4 -> 14 combinations (C_4 = 14)
    res4 = solver.generateParenthesis(4)
    assert len(res4) == 14, f"TC4 failed: expected 14 combinations, got {len(res4)}"
    # Verify all generated strings are unique
    assert len(set(res4)) == 14, "TC4 failed: duplicate combinations found"

    # Test Case 5: Verify correctness of well-formed property for all generated strings
    def is_valid(s: str) -> bool:
        bal = 0
        for ch in s:
            bal += 1 if ch == "(" else -1
            if bal < 0:
                return False
        return bal == 0

    for comb in res4:
        assert is_valid(comb), f"Invalid combination generated: {comb}"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_generate_parenthesis()
