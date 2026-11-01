# Day 34: Find Minimum in Rotated Sorted Array

- **Problem Link:** [LeetCode #153 - Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- **Difficulty:** 🟡 Medium
- **Topic:** Binary Search
- **Date Solved:** 2026-11-01

---

## 📝 Problem Statement

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return the **minimum element** of this array.

You must write an algorithm that runs in **$O(\log n)$ time**.

### Example 1:
```text
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

### Example 2:
```text
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

### Example 3:
```text
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

### Constraints:
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

---

## 💡 Algorithmic Approaches

### 1. Linear Scan (Brute Force)
- Iterate through array and track minimum: `return min(nums)`.
- **Time Complexity:** $O(N)$ — Does not satisfy the $O(\log N)$ constraint.
- **Space Complexity:** $O(1)$.

### 2. Binary Search on Pivot (Optimal) 🚀
- **Key Insight:**
  - A rotated sorted array consists of two sorted subarrays: `[nums[0] ... nums[pivot-1]]` and `[nums[pivot] ... nums[n-1]]`.
  - Every element in the first portion is strictly greater than every element in the second portion.
  - The pivot point `nums[pivot]` is the global minimum.
- **Comparing `nums[mid]` against `nums[right]`:**
  - If `nums[mid] > nums[right]`:
    - The inflection point must lie strictly to the right of `mid`.
    - Hence, the minimum element is in `(mid, right]` $\rightarrow$ update `left = mid + 1`.
  - If `nums[mid] <= nums[right]`:
    - The right half `[mid, right]` is sorted in ascending order.
    - The minimum element could be `nums[mid]` itself or lie in `[left, mid]` $\rightarrow$ update `right = mid`.
- **Termination:**
  - Loop condition `left < right` guarantees convergence to the single minimum index `left == right`.
  - No out-of-bounds or off-by-one errors.

### Complexity:
- **Time Complexity:** $O(\log N)$ — The search range is cut in half at every step.
- **Space Complexity:** $O(1)$ — Only two index pointers used.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
```

---

## 🔑 Binary Search Pivot Trace

```
nums = [4, 5, 6, 7, 0, 1, 2]
Index:  0  1  2  3  4  5  6

Step 1: left = 0, right = 6
        mid = 0 + (6 - 0) // 2 = 3 (nums[3] = 7)
        nums[3] (7) > nums[6] (2) -> inflection in right half -> left = 4

Step 2: left = 4, right = 6
        mid = 4 + (6 - 4) // 2 = 5 (nums[5] = 1)
        nums[5] (1) <= nums[6] (2) -> inflection in left half (incl mid) -> right = 5

Step 3: left = 4, right = 5
        mid = 4 + (5 - 4) // 2 = 4 (nums[4] = 0)
        nums[4] (0) <= nums[5] (1) -> right = 4

Step 4: left = 4, right = 4 -> loop ends!

Result: nums[4] = 0 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard rotation in middle (`[3, 4, 5, 1, 2]` → `1`)
2. Larger array rotation (`[4, 5, 6, 7, 0, 1, 2]` → `0`)
3. Fully sorted (rotated $n$ times) (`[11, 13, 15, 17]` → `11`)
4. Single element boundary (`[1]` → `1`)
5. Two elements rotated (`[2, 1]` → `1`)
6. Two elements already sorted (`[1, 2]` → `1`)
7. Minimum at last index (`[2, 3, 4, 5, 1]` → `1`)
8. Minimum at index 1 (`[5, 1, 2, 3, 4]` → `1`)
9. Mixed positive and negative integers (`[-1, 0, 1, 2, -5, -4, -3, -2]` → `-5`)
10. All negative numbers rotated (`[-3, -2, -1, -5, -4]` → `-5`)
