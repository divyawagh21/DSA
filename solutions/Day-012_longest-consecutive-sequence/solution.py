"""
LeetCode #128: Longest Consecutive Sequence
Difficulty: Medium
Topic: Arrays & Hashing
Date Solved: 2026-10-01

Problem:
Given an unsorted array of integers `nums`, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(N) time.

Example:
  Input:  nums = [100, 4, 200, 1, 3, 2]
  Output: 4    (sequence: 1, 2, 3, 4)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find the longest consecutive integer sequence in O(N) using a Hash Set.

        Intuition:
        A naive approach is to sort nums and scan for runs — O(N log N).
        To achieve O(N) we use a hash set for O(1) lookups.

        Key insight — only START sequences from sequence beginnings:
        A number `n` is the START of a consecutive sequence if and only if
        `n - 1` is NOT in the set. If `n - 1` exists, then `n` is already
        the middle of some longer sequence, and we can skip it. This ensures
        each sequence is processed exactly once.

        Algorithm:
        1. Convert `nums` to a set → O(N) time, O(N) space, enables O(1) lookups.
        2. For each number `n` in the set:
            a. If `n - 1` is in the set, skip (not a sequence start).
            b. Otherwise, count upward: `n+1`, `n+2`, ... as long as each is in
               the set. Record the run length.
        3. Return the maximum run length found.

        Why is this O(N)?
        Each number is "visited" at most twice:
          - Once in the outer loop (to decide whether it's a sequence start).
          - Once in the inner while loop (as part of exactly one sequence).
        Total inner-loop iterations across all outer-loop iterations ≤ N.

        Complexity:
        - Time Complexity: O(N) — set construction O(N) + at most 2N membership
          checks total across both loops.
        - Space Complexity: O(N) — the hash set stores all N numbers.
        """
        if not nums:
            return 0

        num_set = set(nums)
        best = 0

        for n in num_set:
            # Only start counting from the beginning of a sequence
            if n - 1 not in num_set:
                current = n
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                best = max(best, length)

        return best


# --- Unit Tests ---
def test_longest_consecutive():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    assert solver.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4, "TC1 failed"

    # Test Case 2: LeetCode Example 2
    assert solver.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9, "TC2 failed"

    # Test Case 3: Empty array
    assert solver.longestConsecutive([]) == 0, "TC3 failed"

    # Test Case 4: Single element
    assert solver.longestConsecutive([42]) == 1, "TC4 failed"

    # Test Case 5: All elements the same
    assert solver.longestConsecutive([7, 7, 7, 7]) == 1, "TC5 failed"

    # Test Case 6: Already consecutive
    assert solver.longestConsecutive([1, 2, 3, 4, 5]) == 5, "TC6 failed"

    # Test Case 7: Negative numbers included
    assert solver.longestConsecutive([-3, -2, -1, 0, 1]) == 5, "TC7 failed"

    # Test Case 8: Two separate equal-length sequences
    assert solver.longestConsecutive([1, 2, 3, 10, 11, 12]) == 3, "TC8 failed"

    # Test Case 9: Large gap between two sequences of different length
    assert solver.longestConsecutive([1, 2, 3, 4, 100, 101]) == 4, "TC9 failed"

    # Test Case 10: Duplicates in array
    assert solver.longestConsecutive([1, 2, 2, 3]) == 3, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_longest_consecutive()
