# Day 04: Concatenation of Array

- **Problem Link:** [LeetCode #1929 - Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-20

---

## 📝 Problem Statement

Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where:
- `ans[i] == nums[i]`
- `ans[i + n] == nums[i]` for `0 <= i < n`

Specifically, `ans` is the **concatenation** of two `nums` arrays.

Return the array `ans`.

### Example 1:
```text
Input: nums = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

### Example 2:
```text
Input: nums = [1, 3, 2, 1]
Output: [1, 3, 2, 1, 1, 3, 2, 1]
```

### Constraints:
- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

---

## 💡 Algorithmic Approaches

### 1. Index Loop (Explicit)
- Pre-allocate an output list of size `2n`.
- Loop `i` from `0` to `n-1`, setting `ans[i] = nums[i]` and `ans[i + n] = nums[i]`.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

### 2. List Extend
- Start with a copy of `nums`, then `extend` it with `nums` again.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

### 3. List Concatenation / Multiplication (Optimal Pythonic) 🚀
- Use Python's built-in list concatenation: `return nums + nums` (equivalently `nums * 2`).
- Both produce a brand-new list containing all elements of `nums` followed by all elements of `nums` in a single linear pass.
- **Time Complexity:** $O(N)$ — Each element is copied exactly twice.
- **Space Complexity:** $O(N)$ — Only the 2N output list is created.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
```

---

## 🧪 Verification & Test Cases

The solution includes automated unit tests covering:
1. LeetCode Example 1 — `[1, 2, 1]` → `[1, 2, 1, 1, 2, 1]`
2. LeetCode Example 2 — `[1, 3, 2, 1]` → `[1, 3, 2, 1, 1, 3, 2, 1]`
3. Single element array — `[7]` → `[7, 7]`
4. All identical elements — `[5, 5, 5]` → `[5, 5, 5, 5, 5, 5]`
5. Negative numbers — `[-1, 0, 1]` → `[-1, 0, 1, -1, 0, 1]`
6. Large constraint values — `[1000, 999]` → `[1000, 999, 1000, 999]`
7. Input array immutability — verifies the original `nums` is not mutated
