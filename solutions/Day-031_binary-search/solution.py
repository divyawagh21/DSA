"""
LeetCode #704: Binary Search
Difficulty: Easy
Topic: Binary Search
Date Solved: 2026-10-19

Problem:
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`,
write a function to search `target` in `nums`. If `target` exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search for target in sorted array nums using Classic Iterative Binary Search.

        Intuition:
        Because `nums` is sorted in ascending order, comparing the target against the
        middle element allows us to eliminate half of the remaining search space in each step.

        Algorithm:
        1. Maintain search boundary pointers: `left = 0` and `right = len(nums) - 1`.
        2. While `left <= right`:
           - Compute midpoint: `mid = left + (right - left) // 2`.
           - If `nums[mid] == target`: element found, return `mid`.
           - If `nums[mid] < target`: target must lie in the right half, update `left = mid + 1`.
           - If `nums[mid] > target`: target must lie in the left half, update `right = mid - 1`.
        3. If search space is exhausted without a match, return -1.

        Complexity:
        - Time Complexity: O(log N) — Search space is halved on each iteration.
        - Space Complexity: O(1) — Constant auxiliary memory.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# --- Unit Tests ---
def test_search():
    solver = Solution()

    # Test Case 1: Standard case from LeetCode (target present)
    assert solver.search([-1, 0, 3, 5, 9, 12], 9) == 4, "TC1 failed"

    # Test Case 2: Standard case from LeetCode (target absent)
    assert solver.search([-1, 0, 3, 5, 9, 12], 2) == -1, "TC2 failed"

    # Test Case 3: Single element array (target present)
    assert solver.search([5], 5) == 0, "TC3 failed on [5], target 5"

    # Test Case 4: Single element array (target absent)
    assert solver.search([5], -5) == -1, "TC4 failed on [5], target -5"

    # Test Case 5: Target is first element (left boundary)
    assert solver.search([1, 3, 5, 7, 9], 1) == 0, "TC5 failed on left boundary"

    # Test Case 6: Target is last element (right boundary)
    assert solver.search([1, 3, 5, 7, 9], 9) == 4, "TC6 failed on right boundary"

    # Test Case 7: Even length array (target on left-center)
    assert solver.search([2, 4, 6, 8], 4) == 1, "TC7 failed"

    # Test Case 8: Even length array (target on right-center)
    assert solver.search([2, 4, 6, 8], 6) == 2, "TC8 failed"

    # Test Case 9: Target smaller than all elements
    assert solver.search([10, 20, 30], 5) == -1, "TC9 failed"

    # Test Case 10: Target greater than all elements
    assert solver.search([10, 20, 30], 40) == -1, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_search()
