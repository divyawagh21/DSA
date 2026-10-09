"""
LeetCode #424: Longest Repeating Character Replacement
Difficulty: Medium
Topic: Sliding Window
Date Solved: 2026-10-09

Problem:
You are given a string `s` and an integer `k`. You can choose any character of the
string and change it to any other uppercase English character. You can perform this
operation at most `k` times.

Return the length of the longest substring containing the same letter you can get
after performing the above operations.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest uniform substring after at most k character replacements
        using an optimal Sliding Window with Running Max Frequency.

        Intuition:
        For any candidate window [left, right], the number of characters that MUST be
        replaced to make the whole window uniform is:
            replacements_needed = window_length - count(most_frequent_character)

        As long as `replacements_needed <= k`, the window is valid.
        
        Key optimization:
        We do NOT need to recalculate `max_freq` from scratch when shrinking `left`.
        Why? Because our goal is to find the MAXIMUM window length. A smaller `max_freq`
        could only produce a smaller window, which can never beat our best answer so far.
        Thus, `max_freq` only ever needs to increase, leading to a strict O(N) runtime.

        Algorithm:
        1. Expand `right` across `s`, incrementing `counts[s[right]]`.
        2. Update `max_freq = max(max_freq, counts[s[right]])`.
        3. If `(right - left + 1) - max_freq > k`:
           - The window is invalid.
           - Decrement `counts[s[left]]` and increment `left`.
        4. The max valid window size is maintained.

        Complexity:
        - Time Complexity: O(N) — Left and right pointers each advance at most N times.
        - Space Complexity: O(26) = O(1) — At most 26 uppercase English letters in hash map.
        """
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            char = s[right]
            counts[char] += 1
            if counts[char] > max_freq:
                max_freq = counts[char]

            # Current window requires more than k replacements → shrink from left
            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len

        return max_len


# --- Unit Tests ---
def test_character_replacement():
    solver = Solution()

    # Test Case 1: Standard case with 2 replacements
    assert solver.characterReplacement("ABAB", 2) == 4, "TC1 failed ('AAAA' or 'BBBB')"

    # Test Case 2: Multi-character series with 1 replacement
    assert solver.characterReplacement("AABABBA", 1) == 4, "TC2 failed ('AABA' or 'ABBA')"

    # Test Case 3: k = 0 (no replacements allowed)
    assert solver.characterReplacement("ABCDE", 0) == 1, "TC3 failed (k=0 with distinct chars)"

    # Test Case 4: k = 0 with existing duplicates
    assert solver.characterReplacement("ABBBBA", 0) == 4, "TC4 failed (k=0 with identical streak)"

    # Test Case 5: k is larger than string length
    assert solver.characterReplacement("ABC", 10) == 3, "TC5 failed (k >= len(s))"

    # Test Case 6: Single character string
    assert solver.characterReplacement("Z", 1) == 1, "TC6 failed (Single char)"

    # Test Case 7: All characters identical initially
    assert solver.characterReplacement("AAAA", 2) == 4, "TC7 failed (Already uniform)"

    # Test Case 8: Replacement at the start or end
    assert solver.characterReplacement("BAAAB", 2) == 5, "TC8 failed (Surrounding replacements)"

    # Test Case 9: Long repeating sequence with interspersed noises
    assert solver.characterReplacement("KRSCDCSONAJNHLBMAQEZTXCOABG", 3) == 5, "TC9 failed (Sparse noisy string)"

    # Test Case 10: Alternating pattern with k=1
    assert solver.characterReplacement("ABAA", 0) == 2, "TC10 failed ('AA' length 2)"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_character_replacement()
