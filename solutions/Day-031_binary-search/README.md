# Day 31: Binary Search

- **Problem Link:** [LeetCode #704 - Binary Search](https://leetcode.com/problems/binary-search/)
- **Difficulty:** 🟢 Easy
- **Topic:** Binary Search *(New Chapter Begins! 🔍)*
- **Date Solved:** 2026-10-19

---

## 📝 Problem Statement

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with **$O(\log n)$ runtime complexity**.

### Example 1:
```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4.
```

### Example 2:
```text
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1.
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

---

## 💡 Algorithmic Approaches

### 1. Linear Search (Naive)
- Check each element from left to right: `for i in range(len(nums)): if nums[i] == target: return i`.
- **Time Complexity:** $O(N)$ — Does not satisfy the $O(\log N)$ constraint.
- **Space Complexity:** $O(1)$.

### 2. Iterative Binary Search (Optimal) 🚀
- **Key Insight:** In a sorted array, comparing the target against the middle element immediately eliminates **half** of the candidates in each step.
- **Algorithm:**
  1. Maintain two pointers: `left = 0`, `right = len(nums) - 1`.
  2. While `left <= right`:
     - Compute midpoint: `mid = left + (right - left) // 2` (avoids potential integer overflow).
     - If `nums[mid] == target`: Found target, return `mid`.
     - If `nums[mid] < target`: Target must lie in the right half, update `left = mid + 1`.
     - If `nums[mid] > target`: Target must lie in the left half, update `right = mid - 1`.
  3. If search space shrinks to empty (`left > right`), the target does not exist; return `-1`.

### Complexity:
- **Time Complexity:** $O(\log N)$ — The search interval divides by 2 in each iteration.
- **Space Complexity:** $O(1)$ — Iterative pointers use constant memory.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

---

## 🔑 Search Interval Reduction Trace

```
nums = [-1, 0, 3, 5, 9, 12], target = 9

Step 1: left=0 (-1), right=5 (12)
        mid = 0 + (5-0)//2 = 2 (nums[2] = 3)
        3 < 9 -> search right -> left = 3

Step 2: left=3 (5), right=5 (12)
        mid = 3 + (5-3)//2 = 4 (nums[4] = 9)
        9 == 9 -> FOUND! Return index 4 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Target present in interior (`[-1, 0, 3, 5, 9, 12]`, target=9 → `4`)
2. Target absent within range (`[-1, 0, 3, 5, 9, 12]`, target=2 → `-1`)
3. Single element match (`[5]`, target=5 → `0`)
4. Single element miss (`[5]`, target=-5 → `-1`)
5. Target at leftmost index 0 (`[1, 3, 5, 7, 9]`, target=1 → `0`)
6. Target at rightmost index `n-1` (`[1, 3, 5, 7, 9]`, target=9 → `4`)
7. Even-length array left-mid match (`[2, 4, 6, 8]`, target=4 → `1`)
8. Even-length array right-mid match (`[2, 4, 6, 8]`, target=6 → `2`)
9. Target strictly smaller than all elements (`[10, 20, 30]`, target=5 → `-1`)
10. Target strictly greater than all elements (`[10, 20, 30]`, target=40 → `-1`)
