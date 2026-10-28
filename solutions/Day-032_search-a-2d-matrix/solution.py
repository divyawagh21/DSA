"""
LeetCode #74: Search a 2D Matrix
Difficulty: Medium
Topic: Binary Search
Date Solved: 2026-10-28

Problem:
You are given an m x n integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Search for target in an m x n matrix using Single-Pass Binary Search on a Virtual 1D Array.

        Intuition:
        Because each row is sorted and the first element of row (i+1) is strictly greater
        than the last element of row i, the entire 2D matrix can be viewed as a contiguous
        sorted 1D array of length (m * n).

        Virtual Index Mapping:
        For any 1D index `idx` in range [0, m * n - 1]:
            row = idx // n
            col = idx % n
        where `n` is the number of columns.

        Algorithm:
        1. Initialize `left = 0`, `right = m * n - 1`.
        2. While `left <= right`:
           - mid = left + (right - left) // 2
           - Map `mid` to 2D coordinates: `matrix[mid // n][mid % n]`.
           - If element == target: return True.
           - If element < target: search right half (`left = mid + 1`).
           - If element > target: search left half (`right = mid - 1`).
        3. If exhausted, return False.

        Complexity:
        - Time Complexity: O(log(m * n)) — Single binary search over m * n total elements.
        - Space Complexity: O(1) — No flattening array is allocated; only constant pointers used.
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // n][mid % n]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


# --- Unit Tests ---
def test_search_matrix():
    solver = Solution()

    # Test Case 1: Standard case from LeetCode (target present)
    mat1 = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert solver.searchMatrix(mat1, 3) is True, "TC1 failed"

    # Test Case 2: Standard case from LeetCode (target absent)
    assert solver.searchMatrix(mat1, 13) is False, "TC2 failed"

    # Test Case 3: 1x1 matrix (hit)
    assert solver.searchMatrix([[1]], 1) is True, "TC3 failed"

    # Test Case 4: 1x1 matrix (miss)
    assert solver.searchMatrix([[1]], 2) is False, "TC4 failed"

    # Test Case 5: 1xN single row matrix
    assert solver.searchMatrix([[1, 3, 5]], 3) is True, "TC5 failed"
    assert solver.searchMatrix([[1, 3, 5]], 4) is False, "TC5 miss failed"

    # Test Case 6: Mx1 single column matrix
    assert solver.searchMatrix([[1], [3], [5]], 5) is True, "TC6 failed"
    assert solver.searchMatrix([[1], [3], [5]], 2) is False, "TC6 miss failed"

    # Test Case 7: Target smaller than minimum matrix element
    assert solver.searchMatrix(mat1, -5) is False, "TC7 failed"

    # Test Case 8: Target larger than maximum matrix element
    assert solver.searchMatrix(mat1, 100) is False, "TC8 failed"

    # Test Case 9: Target at first element (top-left)
    assert solver.searchMatrix(mat1, 1) is True, "TC9 failed"

    # Test Case 10: Target at last element (bottom-right)
    assert solver.searchMatrix(mat1, 60) is True, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_search_matrix()
