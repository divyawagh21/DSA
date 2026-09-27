"""
LeetCode #238: Product of Array Except Self
Difficulty: Medium
Topic: Arrays & Hashing
Date Solved: 2026-09-27

Problem:
Given an integer array `nums`, return an array `answer` such that `answer[i]`
is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(N) time and without using the
division operation.

Follow-up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Return product of all elements except self using prefix and suffix
        products — O(N) time, O(1) extra space (excluding output array).

        Intuition:
        For each index i, the answer is:
            answer[i] = (product of all elements LEFT of i)
                      * (product of all elements RIGHT of i)

        Naive approach: compute left and right product arrays separately
        (two O(N) passes), then multiply them → O(N) time but O(N) extra space.

        O(1) space optimisation:
        1. First pass (left to right): fill `answer[i]` with the prefix product
           (product of all elements strictly to the LEFT of i).
           - answer[0] = 1 (no elements to the left of index 0).
        2. Second pass (right to left): maintain a running `right` multiplier
           starting at 1. At each index i, multiply answer[i] (which already
           holds the left product) by `right`, then update right *= nums[i].

        After both passes, answer[i] = left_product[i] * right_product[i].

        Complexity:
        - Time Complexity: O(N) — two linear passes over the array.
        - Space Complexity: O(1) extra space — only the output array `answer`
          and a single integer `right` are used; the output array itself is not
          counted per the problem statement.
        """
        n = len(nums)
        answer = [1] * n

        # Pass 1: fill answer[i] with product of all elements to the LEFT of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply answer[i] by product of all elements to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# --- Unit Tests ---
def test_product_except_self():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    assert solver.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6], "TC1 failed"

    # Test Case 2: LeetCode Example 2 — contains zero
    assert solver.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0], "TC2 failed"

    # Test Case 3: Two elements
    assert solver.productExceptSelf([3, 4]) == [4, 3], "TC3 failed"

    # Test Case 4: Array with a single zero
    assert solver.productExceptSelf([1, 0, 3, 4]) == [0, 12, 0, 0], "TC4 failed"

    # Test Case 5: Two zeros — all products become 0
    assert solver.productExceptSelf([0, 0, 2]) == [0, 0, 0], "TC5 failed"

    # Test Case 6: All ones
    assert solver.productExceptSelf([1, 1, 1, 1]) == [1, 1, 1, 1], "TC6 failed"

    # Test Case 7: Contains negative numbers
    assert solver.productExceptSelf([-1, -2, -3, -4]) == [-24, -12, -8, -6], "TC7 failed"

    # Test Case 8: Large values
    assert solver.productExceptSelf([2, 3, 4, 5]) == [60, 40, 30, 24], "TC8 failed"

    # Test Case 9: Mixed positive and negative
    assert solver.productExceptSelf([1, -1, 1, -1]) == [1, -1, 1, -1], "TC9 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_product_except_self()
