"""
LeetCode #392: Is Subsequence
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-23

Problem:
Given two strings `s` and `t`, return true if `s` is a subsequence of `t`,
or false otherwise.

A subsequence of a string is a new string that is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if `s` is a subsequence of `t` using the two-pointer technique.

        Intuition:
        A subsequence maintains the relative order of characters but allows
        skipping characters from `t`. We use two pointers:
        - `sp` tracks our position in `s` (the pattern we are trying to match).
        - `tp` tracks our position in `t` (the source text we scan through).

        At each step, we advance `tp` by 1 always (scan through `t`).
        If `t[tp] == s[sp]`, we also advance `sp` (we matched one character
        of `s`). If `sp` reaches `len(s)`, all characters of `s` have been
        matched in order within `t`, so we return True.

        Edge cases:
        - Empty `s` ("") is a subsequence of any string — return True immediately.
        - If `t` is exhausted before `sp` reaches len(s), return False.

        Follow-up (many queries with same `t`):
        Pre-process `t` into a dictionary mapping each character to the sorted
        list of indices where it appears. For each query `s`, binary search
        (bisect_left) to find the next valid index in `t` for each character of
        `s`. This gives O(|t|) pre-processing and O(|s| log |t|) per query.

        Complexity:
        - Time Complexity: O(N) where N = len(t). We scan `t` at most once.
        - Space Complexity: O(1) — Only two integer pointers are used.
        """
        sp = 0  # pointer into s

        for char in t:
            if sp == len(s):
                break
            if char == s[sp]:
                sp += 1

        return sp == len(s)


# --- Unit Tests ---
def test_is_subsequence():
    solver = Solution()

    # Test Case 1: LeetCode Example 1 — valid subsequence
    assert solver.isSubsequence("ace", "abcde") is True, "TC1 failed"

    # Test Case 2: LeetCode Example 2 — invalid (out of order)
    assert solver.isSubsequence("aec", "abcde") is False, "TC2 failed"

    # Test Case 3: Empty s — always a subsequence of any t
    assert solver.isSubsequence("", "abcde") is True, "TC3 failed"

    # Test Case 4: Empty t — only empty s can be a subsequence
    assert solver.isSubsequence("", "") is True, "TC4 failed"
    assert solver.isSubsequence("a", "") is False, "TC4b failed"

    # Test Case 5: s equals t exactly
    assert solver.isSubsequence("abc", "abc") is True, "TC5 failed"

    # Test Case 6: s longer than t — impossible
    assert solver.isSubsequence("abcde", "abc") is False, "TC6 failed"

    # Test Case 7: Single character — present
    assert solver.isSubsequence("b", "abc") is True, "TC7 failed"

    # Test Case 8: Single character — absent
    assert solver.isSubsequence("z", "abc") is False, "TC8 failed"

    # Test Case 9: All characters match but spread far apart
    assert solver.isSubsequence("axc", "ahbgdc") is False, "TC9 failed"

    # Test Case 10: Duplicate characters in t
    assert solver.isSubsequence("aa", "aabaa") is True, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_is_subsequence()
