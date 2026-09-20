"""
LeetCode #1929: Concatenation of Array
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-20

Problem:
Given an integer array `nums` of length n, you want to create an array `ans`
of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
(0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.
Return the array `ans`.
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Return the concatenation of `nums` with itself.

        Intuition:
        The problem simply asks us to build an array that is `nums` appended to
        itself. Python's list concatenation operator (`+`) creates a new list
        containing all elements of the left operand followed by all elements of
        the right operand, which is exactly what we need in a single O(N) pass.

        Alternative approaches:
        - Slice assignment / extend: `ans = nums[:]; ans.extend(nums)`
        - Index loop: pre-allocate a 2N list and fill positions i and i+n.
        - Built-in multiplication: `nums * 2` (Python shorthand, identical result).

        All approaches are O(N) time and O(N) space, but `nums + nums` (or
        `nums * 2`) is the most idiomatic and concise Python expression.

        Complexity:
        - Time Complexity: O(N) — We iterate through `nums` exactly twice to
          build the 2N output array.
        - Space Complexity: O(N) — The output array `ans` of size 2N is the only
          additional memory used (the problem requires returning a new array).
        """
        return nums + nums


# --- Unit Tests ---
def test_get_concatenation():
    solver = Solution()

    # Test Case 1: Example from LeetCode
    nums1 = [1, 2, 1]
    expected1 = [1, 2, 1, 1, 2, 1]
    result1 = solver.getConcatenation(nums1)
    assert result1 == expected1, f"Failed: expected {expected1}, got {result1}"

    # Test Case 2: Example from LeetCode
    nums2 = [1, 3, 2, 1]
    expected2 = [1, 3, 2, 1, 1, 3, 2, 1]
    result2 = solver.getConcatenation(nums2)
    assert result2 == expected2, f"Failed: expected {expected2}, got {result2}"

    # Test Case 3: Single element array
    nums3 = [7]
    expected3 = [7, 7]
    result3 = solver.getConcatenation(nums3)
    assert result3 == expected3, f"Failed: expected {expected3}, got {result3}"

    # Test Case 4: Array with all identical elements
    nums4 = [5, 5, 5]
    expected4 = [5, 5, 5, 5, 5, 5]
    result4 = solver.getConcatenation(nums4)
    assert result4 == expected4, f"Failed: expected {expected4}, got {result4}"

    # Test Case 5: Array with negative numbers
    nums5 = [-1, 0, 1]
    expected5 = [-1, 0, 1, -1, 0, 1]
    result5 = solver.getConcatenation(nums5)
    assert result5 == expected5, f"Failed: expected {expected5}, got {result5}"

    # Test Case 6: Array with large values (constraint boundary)
    nums6 = [1000, 999]
    expected6 = [1000, 999, 1000, 999]
    result6 = solver.getConcatenation(nums6)
    assert result6 == expected6, f"Failed: expected {expected6}, got {result6}"

    # Test Case 7: Verify original array is not mutated
    nums7 = [4, 5, 6]
    original_copy = nums7[:]
    solver.getConcatenation(nums7)
    assert nums7 == original_copy, "Original array was mutated!"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_get_concatenation()
