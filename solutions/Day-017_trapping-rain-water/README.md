# Day 17: Trapping Rain Water

- **Problem Link:** [LeetCode #42 - Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- **Difficulty:** 🔴 Hard
- **Topic:** Two Pointers / Dynamic Programming
- **Date Solved:** 2026-10-08

---

## 📝 Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

```
       #
   #   ## #
_#_##_######
[0,1,0,2,1,0,1,3,2,1,2,1]
```

### Example 1:
```text
Input:  height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation:
The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (at indices 2, 4, 5, 6, 9, 10) are trapped.
```

### Example 2:
```text
Input:  height = [4, 2, 0, 3, 2, 5]
Output: 9
Explanation:
Water trapped between index 0 (height 4) and index 5 (height 5) amounts to:
(4-2) + (4-0) + (4-3) + (4-2) = 2 + 4 + 1 + 2 = 9 units.
```

### Constraints:
- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- For every bar `i`, scan left to find `max_left[i]` and right to find `max_right[i]`.
- The water trapped above index `i` is `max(0, min(max_left, max_right) - height[i])`.
- **Time Complexity:** $O(N^2)$ — for each element we traverse left and right.
- **Space Complexity:** $O(1)$

### 2. Dynamic Programming (Prefix & Suffix Arrays)
- Precompute `left_max` and `right_max` arrays in two $O(N)$ passes:
  - `left_max[i] = max(left_max[i-1], height[i])`
  - `right_max[i] = max(right_max[i+1], height[i])`
- In a third pass, calculate `water[i] = min(left_max[i], right_max[i]) - height[i]`.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ — requires auxiliary arrays.

### 3. Two Pointers (Optimal) 🚀

#### Core Insight:
We do not actually need the exact values of both `left_max` and `right_max` at index `i`. We only need to identify **which side is the bottleneck**.

- If `left_max < right_max`, the water trapped at `left` is strictly bounded by `left_max` regardless of intermediate bars, because we already know a bar with height at least `right_max > left_max` exists to its right.
- Therefore, we can safely compute trapped water at `left` using `left_max - height[left]` and advance `left += 1`.
- Symmetrically, if `right_max <= left_max`, `right_max` is the bottleneck on the right. We process `right_max - height[right]` and decrement `right -= 1`.

#### Step-by-Step Algorithm:
1. Handle edge cases: if `len(height) < 3`, return `0`.
2. Initialize pointers `left = 0`, `right = n - 1`.
3. Track `left_max = height[left]`, `right_max = height[right]`, `water = 0`.
4. While `left < right`:
   - If `left_max < right_max`:
     - Advance `left += 1`.
     - Update `left_max = max(left_max, height[left])`.
     - Add `left_max - height[left]` to `water`.
   - Else:
     - Advance `right -= 1`.
     - Update `right_max = max(right_max, height[right])`.
     - Add `right_max - height[right]` to `water`.
5. Return `water`.

- **Time Complexity:** $O(N)$ — single pass; pointers meet in the middle.
- **Space Complexity:** $O(1)$ — constant memory.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water
```

---

## 🔑 Pointer Simulation Trace

For `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`:

```
Indices:    0  1  2  3  4  5  6  7  8  9  10 11
Heights:   [0, 1, 0, 2, 1, 0, 1, 3, 2, 1,  2, 1]

l=0 (h=0), r=11 (h=1)  | left_max=0, right_max=1  | left_max < right_max -> l=1, left_max=1,  water += 0
l=1 (h=1), r=11 (h=1)  | left_max=1, right_max=1  | tie -> r=10, right_max=2, water += 0
l=1 (h=1), r=10 (h=2)  | left_max=1, right_max=2  | l=2, left_max=1,  water += (1-0) = 1
l=2 (h=0), r=10 (h=2)  | left_max=1, right_max=2  | l=3, left_max=2,  water += 0
l=3 (h=2), r=10 (h=2)  | left_max=2, right_max=2  | tie -> r=9, right_max=2,  water += (2-1) = 1 (total 2)
l=3 (h=2), r=9  (h=1)  | left_max=2, right_max=2  | tie -> r=8, right_max=2,  water += (2-2) = 0 (total 2)
l=3 (h=2), r=8  (h=2)  | left_max=2, right_max=2  | tie -> r=7, right_max=3,  water += 0 (total 2)
l=3 (h=2), r=7  (h=3)  | left_max=2, right_max=3  | l=4, left_max=2,  water += (2-1) = 1 (total 3)
l=4 (h=1), r=7  (h=3)  | left_max=2, right_max=3  | l=5, left_max=2,  water += (2-0) = 2 (total 5)
l=5 (h=0), r=7  (h=3)  | left_max=2, right_max=3  | l=6, left_max=2,  water += (2-1) = 1 (total 6)
l=6 (h=1), r=7  (h=3)  | left_max=2, right_max=3  | l=7, left_max=3,  water += 0 (total 6)
l=7, r=7 -> Loop terminates.

Total Trapped Water = 6 units ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 11 comprehensive automated test cases:
1. **LeetCode Example 1**: Multi-valley terrain with 6 units trapped.
2. **LeetCode Example 2**: Deep asymmetric trough with 9 units trapped.
3. **Edge cases**: Empty array, single bar, two bars (all 0 trapped).
4. **Monotonic increasing**: Water spills to the left (0 trapped).
5. **Monotonic decreasing**: Water spills to the right (0 trapped).
6. **Flat terrain**: Uniform elevation (0 trapped).
7. **Single symmetrical valley**: `[3, 0, 3]` -> 3 units trapped.
8. **Wide flat pit**: `[5, 1, 1, 1, 5]` -> 12 units trapped.
9. **Stepped interior**: `[4, 2, 3]` -> 1 unit trapped.
10. **Multi-basin landscape**: Validated against both DP and Two-Pointer logic.
11. **Boundary walls with zero interior**: `[10, 0, 0, 10]` -> 20 units trapped.
