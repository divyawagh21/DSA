# Day 05: Replace Elements with Greatest Element on Right Side

- **Problem Link:** [LeetCode #1299 - Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-21

---

## 📝 Problem Statement

Given an array `arr`, replace every element in that array with the greatest element among the elements to its **right**, and replace the **last element** with `-1`.

After doing so, return the array.

### Example 1:
```text
Input:  arr = [17, 18, 5, 4, 6, 1]
Output:       [18,  6, 6, 6, 1,-1]
Explanation:
  - Index 0: max(18,5,4,6,1) = 18
  - Index 1: max(5,4,6,1)    =  6
  - Index 2: max(4,6,1)      =  6
  - Index 3: max(6,1)        =  6
  - Index 4: max(1)          =  1
  - Index 5: (last element)  = -1
```

### Example 2:
```text
Input:  arr = [400]
Output:       [-1]
```

### Constraints:
- `1 <= arr.length <= 10^4`
- `1 <= arr[i] <= 10^5`

---

## 💡 Algorithmic Approaches

### 1. Brute Force — Nested Loops
- For every index `i`, scan all elements `arr[i+1:]` to find the maximum.
- **Time Complexity:** $O(N^2)$ — Inner scan for each outer index.
- **Space Complexity:** $O(1)$

### 2. Right-to-Left Sweep with Running Maximum (Optimal) 🚀
- Traverse the array **right to left**, maintaining a `right_max` variable that tracks the greatest element seen so far to the **right** of the current position.
- At each index `i`:
  1. Compute `new_max = max(right_max, arr[i])` — includes `arr[i]` as a candidate for positions further left.
  2. Set `arr[i] = right_max` — overwrite with the current right-side maximum.
  3. Update `right_max = new_max`.
- Initialize `right_max = -1` so the last element is correctly replaced with `-1`.
- **Time Complexity:** $O(N)$ — Single linear pass.
- **Space Complexity:** $O(1)$ — In-place modification, only two extra variables.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max

        return arr
```

---

## 🧪 Verification & Test Cases

The solution includes 8 automated unit tests covering:
1. LeetCode Example — `[17,18,5,4,6,1]` → `[18,6,6,6,1,-1]`
2. Single element — `[400]` → `[-1]`
3. Strictly increasing array — max is always at the rightmost unvisited position
4. Strictly decreasing array — each element replaced by its immediate right neighbour
5. All identical elements — running max stays constant
6. Two-element array — minimal multi-element case
7. Max at the very beginning — replaced first, cascades correctly
8. Max at second-to-last position — non-trivial mid-array maximum
