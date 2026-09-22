"""
LeetCode #1299: Replace Elements with Greatest Element on Right Side
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-21

Problem:
Given an array `arr`, replace every element in that array with the greatest element
among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Replace each element with the maximum of all elements to its right.
        Replace the last element with -1.

        Intuition:
        A naive approach would scan right from every index to find the max,
        giving O(N^2) time. Instead we use a single right-to-left pass.

        Key insight: if we traverse from the rightmost element leftward, we can
        maintain a running maximum (`right_max`) that tracks the greatest element
        seen so far to the right of the current position.

        Algorithm:
        1. Initialize `right_max = -1` (the value that replaces the last element).
        2. Iterate i from len(arr)-1 down to 0:
            a. Store `new_max = max(right_max, arr[i])`.
               (arr[i] is the value BEFORE we overwrite it, so it becomes a
               candidate for future positions further left)
            b. Overwrite arr[i] with `right_max` (the current max to its right).
            c. Update `right_max = new_max`.
        3. Return the modified array.

        Complexity:
        - Time Complexity: O(N) — A single left-to-right pass over the array.
        - Space Complexity: O(1) — We modify the input array in-place using only
          a constant amount of extra variables.
        """
        right_max = -1  # Sentinel: the last element always becomes -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr


# --- Unit Tests ---
def test_replace_elements():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    arr1 = [17, 18, 5, 4, 6, 1]
    expected1 = [18, 6, 6, 6, 1, -1]
    result1 = solver.replaceElements(arr1)
    assert result1 == expected1, f"TC1 failed: expected {expected1}, got {result1}"

    # Test Case 2: LeetCode Example 2 — single element
    arr2 = [400]
    expected2 = [-1]
    result2 = solver.replaceElements(arr2)
    assert result2 == expected2, f"TC2 failed: expected {expected2}, got {result2}"

    # Test Case 3: Strictly increasing array
    arr3 = [1, 2, 3, 4, 5]
    expected3 = [5, 5, 5, 5, -1]
    result3 = solver.replaceElements(arr3)
    assert result3 == expected3, f"TC3 failed: expected {expected3}, got {result3}"

    # Test Case 4: Strictly decreasing array
    arr4 = [5, 4, 3, 2, 1]
    expected4 = [4, 3, 2, 1, -1]
    result4 = solver.replaceElements(arr4)
    assert result4 == expected4, f"TC4 failed: expected {expected4}, got {result4}"

    # Test Case 5: All identical elements
    arr5 = [7, 7, 7, 7]
    expected5 = [7, 7, 7, -1]
    result5 = solver.replaceElements(arr5)
    assert result5 == expected5, f"TC5 failed: expected {expected5}, got {result5}"

    # Test Case 6: Two elements
    arr6 = [3, 9]
    expected6 = [9, -1]
    result6 = solver.replaceElements(arr6)
    assert result6 == expected6, f"TC6 failed: expected {expected6}, got {result6}"

    # Test Case 7: Max at the beginning
    arr7 = [100, 1, 2, 3]
    expected7 = [3, 3, 3, -1]
    result7 = solver.replaceElements(arr7)
    assert result7 == expected7, f"TC7 failed: expected {expected7}, got {result7}"

    # Test Case 8: Max at the second-to-last position
    arr8 = [1, 2, 99, 3]
    expected8 = [99, 99, 3, -1]
    result8 = solver.replaceElements(arr8)
    assert result8 == expected8, f"TC8 failed: expected {expected8}, got {result8}"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_replace_elements()
