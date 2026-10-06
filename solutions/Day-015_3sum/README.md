# Day 15: 3Sum

- **Problem Link:** [LeetCode #15 - 3Sum](https://leetcode.com/problems/3sum/)
- **Difficulty:** 🟡 Medium
- **Topic:** Two Pointers
- **Date Solved:** 2026-10-06

---

## 📝 Problem Statement

Given an integer array `nums`, return all the **unique triplets** `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must **not contain duplicate triplets**.

### Example 1:
```text
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1,-1,2], [-1,0,1]]
```

### Example 2:
```text
Input:  nums = [0, 1, 1]
Output: []
```

### Example 3:
```text
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

### Constraints:
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

---

## 💡 Algorithm: Sort + Two Pointers

**Key Reduction:** Fix one element `nums[i]` as the anchor. The problem becomes finding a pair in the remaining subarray that sums to `-nums[i]` — exactly Two Sum II (which we solved in Day 14)!

### Steps:
1. **Sort** `nums` → enables two-pointer + easy duplicate skipping.
2. **Outer loop** (anchor `i` from `0` to `n-3`):
   - **Early exit:** If `nums[i] > 0`, all remaining values are positive — no zero-sum triplet possible.
   - **Skip duplicate anchors:** If `nums[i] == nums[i-1]`, continue.
3. **Inner two-pointer** (`left = i+1`, `right = n-1`):
   - `total < 0` → `left++` (need bigger sum)
   - `total > 0` → `right--` (need smaller sum)
   - `total == 0` → record triplet, skip duplicate left/right values, advance both pointers.

### Complexity:
- **Time:** $O(N^2)$ — $O(N \log N)$ sort + $O(N)$ outer × $O(N)$ inner.
- **Space:** $O(1)$ extra (output list excluded).

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1; right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
```

---

## 🔑 Algorithm Trace

```
nums = [-1, 0, 1, 2, -1, -4]
sorted: [-4, -1, -1, 0, 1, 2]

i=0 (anchor=-4):
  left=1(-1), right=5(2) → -3 < 0 → left++
  left=2(-1), right=5(2) → -3 < 0 → left++
  left=3(0),  right=5(2) → -2 < 0 → left++
  left=4(1),  right=5(2) → -1 < 0 → left++  → done

i=1 (anchor=-1):
  left=2(-1), right=5(2) → 0 == 0 → record [-1,-1,2] ✓; advance
  left=3(0),  right=4(1) → 0 == 0 → record [-1,0,1]  ✓; advance
  done

i=2 (anchor=-1): duplicate of i=1 → SKIP

i=3 (anchor=0): 0 > 0? No
  left=4(1), right=5(2) → 3 > 0 → right-- → done

Answer: [[-1,-1,2], [-1,0,1]] ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 9 automated unit tests (order-independent comparison):
1. LeetCode Example 1 — two triplets
2. LeetCode Example 2 — no valid triplet
3. LeetCode Example 3 — all zeros
4. All positive — no triplets
5. All negative — no triplets
6. Duplicate values in input, single unique triplet
7. Four zeros — only one `[0,0,0]` triplet
8. Large mixed array with many duplicates — 6 unique triplets
9. Minimal three-element input
