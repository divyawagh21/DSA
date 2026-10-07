# Day 16: Container With Most Water

- **Problem Link:** [LeetCode #11 - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- **Difficulty:** 🟡 Medium
- **Topic:** Two Pointers
- **Date Solved:** 2026-10-07

---

## 📝 Problem Statement

Given `n` vertical lines where the i-th line has height `height[i]`, find two lines that form a container holding the **maximum amount of water**.

```
Area = min(height[left], height[right]) × (right - left)
```

### Example 1:
```text
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: Lines at index 1 (h=8) and 8 (h=7) → min(8,7) × 7 = 49
```

### Example 2:
```text
Input:  height = [1, 1]
Output: 1
```

### Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Check every pair `(i, j)` and compute the area.
- **Time:** $O(N^2)$ | **Space:** $O(1)$

### 2. Two Pointers — Greedy (Optimal) 🚀

**Greedy Key Insight:**
- Start with the widest possible container: `left=0`, `right=n-1`.
- Area is limited by the **shorter** of the two lines.
- Moving the **taller** line inward: width decreases, height bottleneck stays or decreases → area can only get worse or the same.
- Moving the **shorter** line inward: width decreases, but height bottleneck *might* improve → only option to potentially find a better area.
- Therefore: **always move the pointer at the shorter line**.

**Algorithm:**
1. `left = 0`, `right = n-1`, `best = 0`
2. While `left < right`:
   - `area = min(height[left], height[right]) × (right - left)`
   - `best = max(best, area)`
   - Move shorter pointer inward
3. Return `best`

- **Time Complexity:** $O(N)$ — single pass, pointers meet in the middle.
- **Space Complexity:** $O(1)$ — three variables only.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return best
```

---

## 🔑 Greedy Trace

```
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
          0  1  2  3  4  5  6  7  8

Step 1: l=0(1),  r=8(7)  → min(1,7)×8 = 8   → move l (shorter)
Step 2: l=1(8),  r=8(7)  → min(8,7)×7 = 49  ← best!  → move r (shorter)
Step 3: l=1(8),  r=7(3)  → min(8,3)×6 = 18  → move r
Step 4: l=1(8),  r=6(8)  → min(8,8)×5 = 40  → move l (tie → move l)
Step 5: l=2(6),  r=6(8)  → min(6,8)×4 = 24  → move l
...
Answer: 49 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 9 automated unit tests covering:
1. LeetCode Example 1 — classic case, answer=49
2. LeetCode Example 2 — two-element minimum
3. Strictly increasing heights
4. Strictly decreasing heights
5. All equal heights
6. Large values at both ends, short in middle
7. Peak in the middle — best pair not adjacent
8. Two tall lines with short lines between — answer spans full width
9. Alternating short/tall pattern
