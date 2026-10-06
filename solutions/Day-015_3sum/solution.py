"""
LeetCode #15: 3Sum
Difficulty: Medium
Topic: Two Pointers
Date Solved: 2026-10-06

Problem:
Given an integer array `nums`, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets summing to zero using Sort + Two Pointers.

        Intuition:
        If we fix one element `nums[i]`, the problem reduces to finding two
        numbers in the remaining sorted subarray that sum to `-nums[i]` — exactly
        the Two Sum II problem we know how to solve in O(N) using two pointers.

        Algorithm:
        1. Sort `nums` → O(N log N). Sorting enables:
           a. Two-pointer approach on the inner pair.
           b. Easy duplicate skipping (identical values are adjacent).

        2. Iterate `i` from 0 to n-3 (the "anchor" element):
           a. If nums[i] > 0: since the array is sorted, no triplet can sum to 0
              (all remaining elements are ≥ nums[i] > 0). Break early.
           b. Skip duplicates for `i`: if nums[i] == nums[i-1], continue.
           c. Run two-pointer inner loop:
              - left = i+1, right = n-1
              - Compute total = nums[i] + nums[left] + nums[right].
              - total == 0 → record triplet; skip duplicate left values; skip
                duplicate right values; advance both pointers.
              - total < 0 → left++ (need larger sum).
              - total > 0 → right-- (need smaller sum).

        Why no duplicate triplets?
        - The outer skip (nums[i] == nums[i-1]) prevents reusing the same anchor.
        - The inner skips after finding a triplet prevent reusing same left/right.

        Complexity:
        - Time Complexity: O(N^2) — O(N log N) sort + O(N) outer × O(N) inner.
        - Space Complexity: O(1) extra (not counting the output list). Python's
          sort uses O(log N) stack space.
        """
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Early termination: smallest value is positive → no zero-sum possible
            if nums[i] > 0:
                break

            # Skip duplicate anchor values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


# --- Unit Tests ---
def test_three_sum():
    solver = Solution()

    # Helper: compare regardless of order of triplets and within triplets
    def same(result, expected):
        normalize = lambda lst: sorted([sorted(t) for t in lst])
        return normalize(result) == normalize(expected)

    # Test Case 1: LeetCode Example 1
    assert same(solver.threeSum([-1, 0, 1, 2, -1, -4]),
                [[-1, -1, 2], [-1, 0, 1]]), "TC1 failed"

    # Test Case 2: LeetCode Example 2 — no valid triplets
    assert solver.threeSum([0, 1, 1]) == [], "TC2 failed"

    # Test Case 3: LeetCode Example 3 — all zeros
    assert same(solver.threeSum([0, 0, 0]), [[0, 0, 0]]), "TC3 failed"

    # Test Case 4: All positive — no triplet sums to zero
    assert solver.threeSum([1, 2, 3, 4]) == [], "TC4 failed"

    # Test Case 5: All negative — no triplet sums to zero
    assert solver.threeSum([-3, -2, -1]) == [], "TC5 failed"

    # Test Case 6: Multiple valid triplets with duplicates in input
    assert same(solver.threeSum([-2, 0, 0, 2, 2]),
                [[-2, 0, 2]]), "TC6 failed"

    # Test Case 7: Large duplicate set
    assert same(solver.threeSum([0, 0, 0, 0]),
                [[0, 0, 0]]), "TC7 failed"

    # Test Case 8: Triplet uses all negative values
    assert same(solver.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
                [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
                 [-2, -2, 4], [-2, 0, 2]]), "TC8 failed"

    # Test Case 9: Minimal valid input — single triplet
    assert same(solver.threeSum([-1, 0, 1]), [[-1, 0, 1]]), "TC9 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_three_sum()
