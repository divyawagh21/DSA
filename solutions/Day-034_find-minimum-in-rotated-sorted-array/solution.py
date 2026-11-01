"""
LeetCode #153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search
Date Solved: 2026-11-01

Problem:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in
the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a rotated sorted array using Binary Search in O(log N).

        Intuition:
        In a rotated sorted array with unique elements, there exists a single pivot point
        where nums[i] > nums[i+1]. That nums[i+1] is the minimum element.
        
        Comparing nums[mid] with nums[right]:
        - If nums[mid] > nums[right]:
          The rotation pivot must lie strictly in the right half (mid, right].
          Thus, the minimum element is to the right of mid -> left = mid + 1.
        - If nums[mid] <= nums[right]:
          The right half [mid, right] is sorted normally.
          The minimum element is either nums[mid] itself or lies in the left half [left, mid].
          Thus, right = mid.

        When left == right, both pointers converge to the minimum element.

        Complexity:
        - Time Complexity: O(log N) — Search interval is halved in every iteration.
        - Space Complexity: O(1) — Constant extra memory.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# --- Unit Tests ---
def test_find_min():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    assert solver.findMin([3, 4, 5, 1, 2]) == 1, "TC1 failed"

    # Test Case 2: LeetCode Example 2
    assert solver.findMin([4, 5, 6, 7, 0, 1, 2]) == 0, "TC2 failed"

    # Test Case 3: LeetCode Example 3 (Rotated n times, i.e., fully sorted)
    assert solver.findMin([11, 13, 15, 17]) == 11, "TC3 failed"

    # Test Case 4: Single element array
    assert solver.findMin([1]) == 1, "TC4 failed"

    # Test Case 5: Two elements, rotated
    assert solver.findMin([2, 1]) == 1, "TC5 failed"

    # Test Case 6: Two elements, already sorted
    assert solver.findMin([1, 2]) == 1, "TC6 failed"

    # Test Case 7: Minimum at the very end
    assert solver.findMin([2, 3, 4, 5, 1]) == 1, "TC7 failed"

    # Test Case 8: Minimum at index 1
    assert solver.findMin([5, 1, 2, 3, 4]) == 1, "TC8 failed"

    # Test Case 9: Negative numbers included
    assert solver.findMin([-1, 0, 1, 2, -5, -4, -3, -2]) == -5, "TC9 failed"

    # Test Case 10: All negative numbers, rotated
    assert solver.findMin([-3, -2, -1, -5, -4]) == -5, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_find_min()
