"""
LeetCode #3: Longest Substring Without Repeating Characters
Difficulty: Medium
Topic: Sliding Window
Date Solved: 2026-10-09

Problem:
Given a string `s`, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without duplicate characters
        using a dynamic Sliding Window with Last-Seen Index optimization.

        Intuition:
        A substring must be contiguous. If we maintain a sliding window [left, right]
        where all characters inside the window are strictly unique:
        - We expand the window by advancing `right` across the string.
        - If the character at `right` has already been seen inside our current window
          (i.e., its last recorded index >= left), we must contract the window by
          jumping `left` directly to `last_seen[s[right]] + 1`.
        - We update `last_seen[s[right]] = right`.
        - The current valid window length is `right - left + 1`.

        Why jumping `left` is optimal:
        Instead of removing characters from a set one by one with a while-loop (which
        would touch each element up to twice), storing the last-seen index allows `left`
        to jump directly to the valid position in O(1), achieving a single strict linear pass.

        Complexity:
        - Time Complexity: O(N) — Every character in `s` is visited once by the right pointer.
        - Space Complexity: O(min(N, M)) — Hash map stores up to min(length of string, size of character set).
        """
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                # Character repeated within current window — jump left pointer
                left = last_seen[char] + 1

            last_seen[char] = right
            window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len

        return max_len


# --- Unit Tests ---
def test_length_of_longest_substring():
    solver = Solution()

    # Test Case 1: Standard case with repeating pattern
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3, "TC1 failed ('abc' length 3)"

    # Test Case 2: All identical characters
    assert solver.lengthOfLongestSubstring("bbbbb") == 1, "TC2 failed ('b' length 1)"

    # Test Case 3: Substring in the middle
    assert solver.lengthOfLongestSubstring("pwwkew") == 3, "TC3 failed ('wke' length 3)"

    # Test Case 4: Empty string
    assert solver.lengthOfLongestSubstring("") == 0, "TC4 failed (Empty string)"

    # Test Case 5: Single character
    assert solver.lengthOfLongestSubstring(" ") == 1, "TC5 failed (Single space)"

    # Test Case 6: All distinct characters
    assert solver.lengthOfLongestSubstring("abcdef") == 6, "TC6 failed (All distinct)"

    # Test Case 7: Alternating characters
    assert solver.lengthOfLongestSubstring("abba") == 2, "TC7 failed ('ab' or 'ba')"

    # Test Case 8: Mixed digits, letters, and symbols
    assert solver.lengthOfLongestSubstring("a!b@c#1$2%3^") == 12, "TC8 failed (Special chars)"

    # Test Case 9: Repetition with spaces
    assert solver.lengthOfLongestSubstring("tmmzuxt") == 5, "TC9 failed ('mzuxt' length 5)"

    # Test Case 10: Two characters repeated
    assert solver.lengthOfLongestSubstring("dvdf") == 3, "TC10 failed ('vdf' length 3)"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_length_of_longest_substring()
