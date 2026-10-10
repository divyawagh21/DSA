"""
LeetCode #76: Minimum Window Substring
Difficulty: Hard
Topic: Sliding Window
Date Solved: 2026-10-10

Problem:
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum
window substring of `s` such that every character in `t` (including duplicates) is
included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find the minimum window in s containing all characters of t using an optimal
        Variable-Size Sliding Window with a Match Counter.

        Intuition:
        We need the smallest contiguous window [left, right] in `s` that covers all
        characters and frequencies required by `t`.

        Instead of checking all required characters on each step (which could be O(|unique(t)|)),
        we track:
        - `target_counts`: frequency map of characters in `t`.
        - `required`: number of UNIQUE characters in `t` that must meet their target frequency.
        - `formed`: number of UNIQUE characters currently satisfying their target frequency in the window.

        Two-Phase Window Movement:
        1. Expansion Phase (Move `right`):
           Advance `right` to include characters until `formed == required` (window is valid).
        2. Contraction Phase (Move `left`):
           While the window remains valid (`formed == required`):
           - Record the window length and boundaries if smaller than the current best.
           - Advance `left` to remove redundant characters and minimize window size.
           - If removing `s[left]` drops its count below what `t` requires, decrement `formed`
             and break back to the expansion phase.

        Complexity:
        - Time Complexity: O(M + N) where M = len(s) and N = len(t).
          `right` visits each character in `s` once, and `left` visits each character at most once.
        - Space Complexity: O(M + N) to store character counts in the hash maps (at most O(52) = O(1)
          if restricted to English letters).
        """
        if not s or not t:
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts = defaultdict(int)
        formed = 0

        # Tuple: (window_length, left_idx, right_idx)
        best_window = (float("inf"), None, None)
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            # If the frequency of the current character matches its target in t
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Try contracting the window from the left while it is valid
            while formed == required and left <= right:
                window_len = right - left + 1
                if window_len < best_window[0]:
                    best_window = (window_len, left, right)

                # Character leaving the window
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1

                left += 1

        if best_window[0] == float("inf"):
            return ""

        return s[best_window[1]:best_window[2] + 1]


# --- Unit Tests ---
def test_min_window():
    solver = Solution()

    # Test Case 1: Standard case with non-trivial contraction
    assert solver.minWindow("ADOBECODEBANC", "ABC") == "BANC", "TC1 failed"

    # Test Case 2: Exact single character match
    assert solver.minWindow("a", "a") == "a", "TC2 failed"

    # Test Case 3: Impossible match (target character missing)
    assert solver.minWindow("a", "aa") == "", "TC3 failed"

    # Test Case 4: Target string longer than source string
    assert solver.minWindow("ab", "abc") == "", "TC4 failed"

    # Test Case 5: Target requires duplicate characters
    assert solver.minWindow("AABBCC", "AAB") == "AAB", "TC5 failed"

    # Test Case 6: Target matches entire source string
    assert solver.minWindow("HELLO", "HELLO") == "HELLO", "TC6 failed"

    # Test Case 7: Minimum window located at the very start
    assert solver.minWindow("ABXYZCD", "AB") == "AB", "TC7 failed"

    # Test Case 8: Minimum window located at the very end
    assert solver.minWindow("XYZABCD", "CD") == "CD", "TC8 failed"

    # Test Case 9: Dispersed target characters with shortest window
    assert solver.minWindow("AAABBBCCOAABBCC", "ABC") == "ABBC", "TC9 failed"

    # Test Case 10: Mixed case sensitivity
    assert solver.minWindow("aAbBcC", "AB") == "AbB", "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_min_window()
