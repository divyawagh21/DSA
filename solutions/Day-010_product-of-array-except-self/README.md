# Day 10: Product of Array Except Self

- **Problem Link:** [LeetCode #238 - Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- **Difficulty:** 🟡 Medium
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-27

---

## 📝 Problem Statement

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the **product of all the elements of `nums` except `nums[i]`**.

> **Constraints:** Must run in $O(N)$ time. **Division is not allowed.**
> **Follow-up:** Solve in $O(1)$ extra space (output array excluded).

### Example 1:
```text
Input:  nums   = [1, 2, 3, 4]
Output: answer = [24, 12, 8, 6]
```

### Example 2:
```text
Input:  nums   = [-1, 1, 0, -3, 3]
Output: answer = [0, 0, 9, 0, 0]
```

### Constraints:
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a **32-bit integer**.

---

## 💡 Algorithmic Approaches

### 1. Using Division (Not Allowed)
- Compute total product; divide by `nums[i]` for each index.
- Breaks for zeros and is explicitly forbidden.

### 2. Separate Prefix & Suffix Arrays
- Build `left[i]` = product of all elements before index `i`.
- Build `right[i]` = product of all elements after index `i`.
- `answer[i] = left[i] * right[i]`.
- **Time:** $O(N)$ | **Space:** $O(N)$ extra

### 3. Two-Pass In-Place (Optimal) 🚀
- **Pass 1 (left → right):** Store running prefix product directly in `answer[i]`.
  - `answer[0] = 1` (nothing to the left of index 0).
- **Pass 2 (right → left):** Maintain a `suffix` integer and multiply it into `answer[i]`.
- The output array stores left products after pass 1; after pass 2 it holds `left[i] * right[i]`.
- **Time Complexity:** $O(N)$ — two linear passes.
- **Space Complexity:** $O(1)$ extra — only the output array + one running variable.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Pass 1: answer[i] = product of all elements LEFT of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply by product of all elements RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
```

---

## 🧪 Verification & Test Cases

The solution includes 9 automated unit tests covering:
1. LeetCode Example 1 — `[1,2,3,4]` → `[24,12,8,6]`
2. LeetCode Example 2 — array with zeros and negatives
3. Two-element array — minimal case
4. Single zero in array — only that position gets non-zero
5. Two zeros — all products become 0
6. All ones — products stay 1
7. All negatives — sign alternation
8. Larger values for full product verification
9. Mixed positive and negative

---

## 🔑 Key Insight Visualised

```
nums     =  [ 1,  2,  3,  4]

After Pass 1 (prefix products):
answer   =  [ 1,  1,  2,  6]   ← left products

Suffix multipliers (right → left):
suffix   =  24, 12,  4,  1

After Pass 2:
answer   =  [24, 12,  8,  6]   ✓
```
