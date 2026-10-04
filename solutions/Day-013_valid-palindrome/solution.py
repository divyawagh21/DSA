"""
LeetCode #125: Valid Palindrome
Difficulty: Easy
Topic: Two Pointers
Date Solved: 2026-10-04

Problem:
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if `s` is a palindrome using the Two-Pointer technique with
        in-place alphanumeric filtering — O(N) time, O(1) extra space.

        Intuition:
        The brute-force approach would clean the string first (filter and
        lowercase), then reverse and compare — O(N) time but O(N) extra space
        for the cleaned copy.

        The optimal approach uses two pointers `left` and `right` starting at
        opposite ends of the original string:
        - Skip any non-alphanumeric characters by advancing the pointer inward.
        - Once both pointers point to valid alphanumeric characters, compare
          them (case-insensitively).
        - If they differ → not a palindrome → return False.
        - If they match → advance both pointers inward and continue.
        - When left >= right, all characters matched → return True.

        This avoids creating any intermediate string, using only two integer
        pointers as auxiliary storage.

        Complexity:
        - Time Complexity: O(N) — each character is visited at most once
          (from the left or the right, but never both).
        - Space Complexity: O(1) — only two integer pointers; no cleaned string.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Advance left past non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            # Advance right past non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two valid characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# --- Unit Tests ---
def test_is_palindrome():
    solver = Solution()

    # Test Case 1: LeetCode Example 1 — classic palindrome with spaces/punctuation
    assert solver.isPalindrome("A man, a plan, a canal: Panama") is True, "TC1 failed"

    # Test Case 2: LeetCode Example 2 — not a palindrome
    assert solver.isPalindrome("race a car") is False, "TC2 failed"

    # Test Case 3: LeetCode Example 3 — empty or whitespace only
    assert solver.isPalindrome(" ") is True, "TC3 failed"

    # Test Case 4: Single character — always palindrome
    assert solver.isPalindrome("a") is True, "TC4 failed"

    # Test Case 5: Two identical characters
    assert solver.isPalindrome("aa") is True, "TC5 failed"

    # Test Case 6: Two different characters
    assert solver.isPalindrome("ab") is False, "TC6 failed"

    # Test Case 7: Numbers in string
    assert solver.isPalindrome("0P") is False, "TC7 failed"

    # Test Case 8: Pure digit palindrome
    assert solver.isPalindrome("12321") is True, "TC8 failed"

    # Test Case 9: Mixed alphanumeric palindrome
    assert solver.isPalindrome("A1 1a") is True, "TC9 failed"

    # Test Case 10: Entirely non-alphanumeric → empty after filtering → palindrome
    assert solver.isPalindrome(".,!?") is True, "TC10 failed"

    # Test Case 11: Long palindrome sentence
    assert solver.isPalindrome("Was it a car or a cat I saw?") is True, "TC11 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_is_palindrome()
