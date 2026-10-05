# Day 14: Two Sum II - Input Array Is Sorted

- **Problem Link:** [LeetCode #167 - Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- **Difficulty:** 🟡 Medium
- **Topic:** Two Pointers
- **Date Solved:** 2026-10-05

---

## 📝 Problem Statement

Given a **1-indexed** array of integers `numbers` sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number.

Return `[index1, index2]` (1-indexed). The solution must use **only constant extra space**.

### Example 1:
```text
Input:  numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: 2 + 7 = 9
```

### Example 2:
```text
Input:  numbers = [2, 3, 4], target = 6
Output: [1, 3]
```

### Example 3:
```text
Input:  numbers = [-1, 0], target = -1
Output: [1, 2]
```

### Constraints:
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- Exactly one solution exists.
- Cannot use the same element twice.
- Must use $O(1)$ extra space.

---

## 💡 Algorithmic Approaches

### 1. Hash Map (Two Sum I approach)
- Store values seen so far in a dict; check `target - numbers[i]`.
- **Time:** $O(N)$ | **Space:** $O(N)$ — violates constant-space constraint.

### 2. Binary Search
- For each `numbers[i]`, binary search for `target - numbers[i]` in the remaining array.
- **Time:** $O(N \log N)$ | **Space:** $O(1)$

### 3. Two Pointers (Optimal) 🚀
- Sorted order lets us directly drive the sum up or down:
  - `left` starts at index 0, `right` at last index.
  - `sum < target` → move `left` right (increase sum).
  - `sum > target` → move `right` left (decrease sum).
  - `sum == target` → return `[left+1, right+1]` (1-indexed).
- **Time Complexity:** $O(N)$ — at most one full pass.
- **Space Complexity:** $O(1)$ — only two pointers.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []
```

---

## 🔑 Two-Pointer Trace

```
numbers = [2, 7, 11, 15], target = 9

Step 1: left=0(2), right=3(15) → sum=17 > 9 → right--
Step 2: left=0(2), right=2(11) → sum=13 > 9 → right--
Step 3: left=0(2), right=1(7)  → sum=9  = 9 → return [1, 2] ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests covering:
1. LeetCode Example 1 — `[2,7,11,15]`, target=9 → `[1,2]`
2. LeetCode Example 2 — `[2,3,4]`, target=6 → `[1,3]`
3. LeetCode Example 3 — negative numbers
4. Target at last two elements
5. Target at first two elements
6. Two-element array (minimum size)
7. Mixed negative and positive
8. Larger array
9. Array with duplicate values
10. Target found in middle of array
