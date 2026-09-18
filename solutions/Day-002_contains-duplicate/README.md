# Day 02: Contains Duplicate

- **Problem Link:** [LeetCode #217 - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-18

---

## 📝 Problem Statement

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
```text
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.
```

### Example 2:
```text
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.
```

### Example 3:
```text
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Compare every pair of elements using nested loops `(i, j)`.
- If `nums[i] == nums[j]`, return `true`.
- **Time Complexity:** $O(N^2)$ (Causes Time Limit Exceeded for $N = 10^5$)
- **Space Complexity:** $O(1)$

### 2. Sorting
- Sort the array in ascending order.
- Linearly scan adjacent pairs `nums[i] == nums[i+1]`.
- **Time Complexity:** $O(N \log N)$
- **Space Complexity:** $O(1)$ or $O(N)$ depending on Python's Timsort.

### 3. Hash Set (Early Exit) — Optimal 🚀
- Traverse `nums` while tracking seen values in a hash set.
- Check if `num in seen`:
  - If **yes**, immediately return `true` (short-circuiting unnecessary iterations).
  - If **no**, add `num` to `seen`.
- If the loop completes without finding a duplicate, return `false`.
- **Time Complexity:** $O(N)$ worst case, $O(K)$ average case where $K$ is the index of the first duplicate.
- **Space Complexity:** $O(N)$ to store up to $N$ unique elements.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

---

## 🧪 Verification & Test Cases

The solution includes a comprehensive test suite covering:
1. Standard duplicate at boundaries (`[1, 2, 3, 1]`)
2. Completely distinct elements (`[1, 2, 3, 4]`)
3. Highly redundant duplicate arrays (`[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`)
4. Single-element array boundary condition (`[42]`)
5. Two identical elements (`[7, 7]`)
6. Negative numbers and zero (`[-1, 0, 1, -1]`)
7. Extreme constraint values (`[10^9, -10^9, 10^9]`)
