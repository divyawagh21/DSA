"""
LeetCode #167: Two Sum II - Input Array Is Sorted
Difficulty: Medium
Topic: Two Pointers
Date Solved: 2026-10-05

Problem:
Given a 1-indexed array of integers `numbers` that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Your solution must use only constant extra space.
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two indices whose values sum to `target` using Two Pointers — O(N)
        time, O(1) extra space, exploiting the sorted order of the input.

        Intuition:
        Because the array is sorted, we can use the Two-Pointer technique:
        - Place `left` at the start (index 0) and `right` at the end (index n-1).
        - Compute `current_sum = numbers[left] + numbers[right]`.
          - If current_sum == target → found! Return [left+1, right+1] (1-indexed).
          - If current_sum < target → we need a larger sum → advance `left` right.
          - If current_sum > target → we need a smaller sum → advance `right` left.

        Why this works:
        Sorted order guarantees that moving `left` rightward increases the sum
        and moving `right` leftward decreases it. The problem guarantees exactly
        one solution, so we will always find it.

        Why not use a hash map (like Two Sum I)?
        A hash map would use O(N) extra space. The Two-Pointer approach uses
        O(1) extra space, satisfying the problem's constant-space constraint.

        Complexity:
        - Time Complexity: O(N) — at most N iterations; left + right together
          traverse the array at most once.
        - Space Complexity: O(1) — only two integer pointers.
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-indexed
            elif current_sum < target:
                left += 1   # Need a larger sum → move left pointer right
            else:
                right -= 1  # Need a smaller sum → move right pointer left

        # Problem guarantees a solution exists; this line is never reached
        return []


# --- Unit Tests ---
def test_two_sum():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    assert solver.twoSum([2, 7, 11, 15], 9) == [1, 2], "TC1 failed"

    # Test Case 2: LeetCode Example 2
    assert solver.twoSum([2, 3, 4], 6) == [1, 3], "TC2 failed"

    # Test Case 3: LeetCode Example 3 — negative numbers
    assert solver.twoSum([-1, 0], -1) == [1, 2], "TC3 failed"

    # Test Case 4: Target using last two elements
    assert solver.twoSum([1, 2, 3, 4, 5], 9) == [4, 5], "TC4 failed"

    # Test Case 5: Target using first two elements
    assert solver.twoSum([1, 2, 3, 4, 5], 3) == [1, 2], "TC5 failed"

    # Test Case 6: Two elements only
    assert solver.twoSum([5, 10], 15) == [1, 2], "TC6 failed"

    # Test Case 7: Negative and positive mix (-4+7=3 → [1,5])
    assert solver.twoSum([-4, -1, 0, 3, 7], 3) == [1, 5], "TC7 failed"

    # Test Case 8: Larger sorted array (5+11=16 → [3,6])
    assert solver.twoSum([1, 3, 5, 7, 9, 11], 16) == [3, 6], "TC8 failed"

    # Test Case 9: Duplicates in array
    assert solver.twoSum([1, 1, 2, 4], 2) == [1, 2], "TC9 failed"

    # Test Case 10: Target found in middle (2+8=10 → [2,5])
    assert solver.twoSum([1, 2, 4, 6, 8], 10) == [2, 5], "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_two_sum()
