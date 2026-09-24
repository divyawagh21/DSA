"""
LeetCode #58: Length of Last Word
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-24

Problem:
Given a string `s` consisting of words and spaces, return the length of the
last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Calculates the length of the last word by scanning backwards.

        Intuition:
        Since we only care about the last word, scanning backwards from the end
        of the string avoids processing earlier words and prevents allocating
        extra memory for split tokens.

        Algorithm:
        1. Initialize a pointer `i` at the last index: `len(s) - 1`.
        2. Skip all trailing whitespace by decrementing `i` while `s[i] == ' '`.
        3. Count consecutive non-space characters while `i >= 0` and `s[i] != ' '`.
        4. Return the counted length.

        Complexity:
        - Time Complexity: O(N) worst-case (when entire string is traversed),
          but practically O(K) where K is the number of trailing spaces plus
          the length of the last word.
        - Space Complexity: O(1) auxiliary space (no string allocations).
        """
        i = len(s) - 1
        length = 0

        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Step 2: Count characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

    def lengthOfLastWordPythonic(self, s: str) -> int:
        """
        Alternative Pythonic one-liner using rstrip.
        Time: O(N), Space: O(N) worst-case due to slicing/strip.
        """
        return len(s.rstrip().split(" ")[-1])


# --- Unit Tests ---
def test_length_of_last_word():
    solver = Solution()

    # Test Case 1: LeetCode Example 1 — standard case
    assert solver.lengthOfLastWord("Hello World") == 5, "TC1 failed"
    assert solver.lengthOfLastWordPythonic("Hello World") == 5, "TC1 pythonic failed"

    # Test Case 2: LeetCode Example 2 — multiple trailing and leading spaces
    assert (
        solver.lengthOfLastWord("   fly me   to   the moon  ") == 4
    ), "TC2 failed"
    assert (
        solver.lengthOfLastWordPythonic("   fly me   to   the moon  ") == 4
    ), "TC2 pythonic failed"

    # Test Case 3: LeetCode Example 3 — long last word with spaces
    assert (
        solver.lengthOfLastWord("luffy is still joyboy") == 6
    ), "TC3 failed"
    assert (
        solver.lengthOfLastWordPythonic("luffy is still joyboy") == 6
    ), "TC3 pythonic failed"

    # Test Case 4: Single word without spaces
    assert solver.lengthOfLastWord("a") == 1, "TC4 failed"
    assert solver.lengthOfLastWord("algorithm") == 9, "TC4b failed"

    # Test Case 5: Single word with surrounding spaces
    assert solver.lengthOfLastWord("   code   ") == 4, "TC5 failed"

    # Test Case 6: Trailing single character
    assert solver.lengthOfLastWord("hello world a") == 1, "TC6 failed"

    # Test Case 7: Many spaces between words
    assert solver.lengthOfLastWord("foo        bar") == 3, "TC7 failed"

    # Test Case 8: Repeated letters in last word
    assert solver.lengthOfLastWord("test zzzzzzzzzz") == 10, "TC8 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_length_of_last_word()
