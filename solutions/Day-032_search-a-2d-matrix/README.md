# Day 32: Search a 2D Matrix

- **Problem Link:** [LeetCode #74 - Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- **Difficulty:** 🟡 Medium
- **Topic:** Binary Search
- **Date Solved:** 2026-10-28

---

## 📝 Problem Statement

You are given an `m x n` integer matrix `matrix` with the following two properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is strictly greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in **$O(\log(m \cdot n))$ time complexity**.

### Example 1:
```text
Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 3
Output: true
```

### Example 2:
```text
Input: matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 13
Output: false
```

### Constraints:
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

---

## 💡 Algorithmic Approaches

### 1. Two-Pass Binary Search
- Perform a binary search on the first elements of each row to identify the single candidate row.
- Then perform a second binary search within that row.
- **Time Complexity:** $O(\log m + \log n) = O(\log(m \cdot n))$.
- **Space Complexity:** $O(1)$.

### 2. Single-Pass Virtual 1D Binary Search (Optimal) 🚀
- **Key Insight:** The matrix properties guarantee that the 2D matrix is simply a sorted 1D array of length $m \times n$ formatted into rows of length $n$.
- We can perform a standard binary search directly over index range $[0, m \cdot n - 1]$ by translating 1D indices to 2D indices on the fly:
  $$\text{row} = \text{mid} // n, \quad \text{col} = \text{mid} \% n$$
- **Algorithm:**
  1. `left = 0`, `right = m * n - 1`.
  2. While `left <= right`:
     - `mid = left + (right - left) // 2`.
     - `val = matrix[mid // n][mid % n]`.
     - If `val == target`: return `true`.
     - If `val < target`: `left = mid + 1`.
     - If `val > target`: `right = mid - 1`.
  3. Return `false` if not found.

### Complexity:
- **Time Complexity:** $O(\log(m \cdot n))$ — Search interval splits in half on every step.
- **Space Complexity:** $O(1)$ — No flattening array is created; coordinates are converted mathematically in constant time.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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
```

---

## 🔑 Coordinate Mapping Trace

```
Matrix dimensions: m = 3, n = 4 (Total elements = 12)
Target = 3

left = 0, right = 11
mid = 5 -> row = 5 // 4 = 1, col = 5 % 4 = 1 -> matrix[1][1] = 11
11 > 3 -> search left half -> right = 4

left = 0, right = 4
mid = 2 -> row = 2 // 4 = 0, col = 2 % 4 = 2 -> matrix[0][2] = 5
5 > 3 -> search left half -> right = 1

left = 0, right = 1
mid = 0 -> row = 0 // 4 = 0, col = 0 % 4 = 0 -> matrix[0][0] = 1
1 < 3 -> search right half -> left = 1

left = 1, right = 1
mid = 1 -> row = 1 // 4 = 0, col = 1 % 4 = 1 -> matrix[0][1] = 3
3 == 3 -> FOUND! Return true ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard LeetCode example (target present)
2. Standard LeetCode example (target absent)
3. $1 \times 1$ matrix (hit)
4. $1 \times 1$ matrix (miss)
5. $1 \times N$ single row matrix (hit & miss)
6. $M \times 1$ single column matrix (hit & miss)
7. Target smaller than matrix minimum
8. Target larger than matrix maximum
9. Target at top-left corner (first element)
10. Target at bottom-right corner (last element)
