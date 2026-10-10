"""
LeetCode #567: Permutation in String
Difficulty: Medium
Topic: Sliding Window
Date Solved: 2026-10-10

Problem:
Given two strings `s1` and `s2`, return true if `s2` contains a permutation of `s1`,
or false otherwise.

In other words, return true if one of `s1`'s permutations is the substring of `s2`.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Determine if s2 contains any permutation of s1 using a Fixed-Size Sliding Window
        optimized with an O(1) Match Counter.

        Intuition:
        A permutation of `s1` must have:
        1. Exactly the same length as `s1` (let k = len(s1)).
        2. Exactly the same character frequencies as `s1`.

        Thus, the problem is equivalent to finding a contiguous window of length k in `s2`
        that has the identical character count array as `s1`.

        Instead of comparing all 26 frequency counts on every slide (which takes O(26) = O(1),
        but has higher constant factor), we maintain a running `matches` count representing
        how many of the 26 characters currently have matching counts between the window and s1.
        - When matches == 26, the current window is an exact permutation of s1 -> return True!
        - As the window slides:
          - We add the new incoming character on the right: update matches.
          - We remove the outgoing character on the left: update matches.

        Complexity:
        - Time Complexity: O(N) where N = len(s2). We initialize in O(k) and slide in O(1) per step.
        - Space Complexity: O(1) auxiliary space (fixed arrays of size 26 for lowercase English letters).
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        # Initialize counts for s1 and the first window of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1

        # Count initial matching character frequencies
        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1

        # Slide the window across s2
        for r in range(n1, n2):
            if matches == 26:
                return True

            # Incoming character at right
            idx_in = ord(s2[r]) - ord("a")
            s2_counts[idx_in] += 1
            if s2_counts[idx_in] == s1_counts[idx_in]:
                matches += 1
            elif s2_counts[idx_in] == s1_counts[idx_in] + 1:
                matches -= 1

            # Outgoing character at left
            l = r - n1
            idx_out = ord(s2[l]) - ord("a")
            s2_counts[idx_out] -= 1
            if s2_counts[idx_out] == s1_counts[idx_out]:
                matches += 1
            elif s2_counts[idx_out] == s1_counts[idx_out] - 1:
                matches -= 1

        return matches == 26


# --- Unit Tests ---
def test_check_inclusion():
    solver = Solution()

    # Test Case 1: Standard positive case (permutation exists at beginning)
    assert solver.checkInclusion("ab", "eidbaooo") is True, "TC1 failed ('ba' is permutation of 'ab')"

    # Test Case 2: Standard negative case (characters dispersed)
    assert solver.checkInclusion("ab", "eidboaoo") is False, "TC2 failed (no contiguous permutation)"

    # Test Case 3: s1 longer than s2
    assert solver.checkInclusion("abcde", "ab") is False, "TC3 failed (s1 longer than s2)"

    # Test Case 4: s1 and s2 identical
    assert solver.checkInclusion("abc", "abc") is True, "TC4 failed (exact match)"

    # Test Case 5: Permutation at the very end of s2
    assert solver.checkInclusion("adc", "dcda") is True, "TC5 failed ('cda' contains 'adc')"

    # Test Case 6: Single character match
    assert solver.checkInclusion("a", "a") is True, "TC6 failed (single char match)"

    # Test Case 7: Single character mismatch
    assert solver.checkInclusion("a", "b") is False, "TC7 failed (single char mismatch)"

    # Test Case 8: Repeated characters in s1
    assert solver.checkInclusion("hello", "ooolleoooleh") is False, "TC8 failed (frequency mismatch)"

    # Test Case 9: Repeated characters match
    assert solver.checkInclusion("aab", "baab") is True, "TC9 failed ('baa' or 'aab' present)"

    # Test Case 10: Permutation in middle of longer string
    assert solver.checkInclusion("xyz", "afkzxye") is True, "TC10 failed ('zxy' is permutation of 'xyz')"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_check_inclusion()
