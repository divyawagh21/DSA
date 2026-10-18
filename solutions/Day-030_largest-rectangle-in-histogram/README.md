# Day 30: Largest Rectangle in Histogram

- **Problem Link:** [LeetCode #84 - Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- **Difficulty:** 🔴 Hard
- **Topic:** Stack *(Milestone: Day 30 & Stack Topic Complete! 🎉)*
- **Date Solved:** 2026-10-18

---

## 📝 Problem Statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the **largest rectangle in the histogram**.

### Example 1:
```text
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units (formed by heights 5 and 6 of width 2).
```

### Example 2:
```text
Input: heights = [2,4]
Output: 4
```

### Constraints:
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- For every pair of indices `(i, j)`, calculate the area as $\min(\text{heights}[i \dots j]) \times (j - i + 1)$.
- Alternatively, for each bar $i$, expand left and right to find where bars become strictly shorter.
- **Time Complexity:** $O(N^2)$ — Times out for $N = 10^5$ ($10^{10}$ operations).
- **Space Complexity:** $O(1)$.

### 2. Monotonic Increasing Stack (Optimal) 🚀
- **Key Insight:** A rectangle's height is bounded by the shortest bar in its span. For each bar `h`, we want to find the farthest it can stretch left and right.
- Maintain a stack of pairs: `(index, height)` in strictly increasing order of height.
- **Algorithm:**
  1. For each bar $(i, h)$:
     - Set `start = i`.
     - While the stack is non-empty and the top bar is taller than $h$ (`stack[-1][1] > h`):
       - The taller bar on the stack cannot extend further right past index $i$.
       - Pop `(prev_idx, prev_h)` and evaluate rectangle: $\text{area} = \text{prev\_h} \times (i - \text{prev\_idx})$.
       - **Crucial Step:** The current shorter bar $h$ can extend *backwards* to `prev_idx` because the popped bar was taller! Update `start = prev_idx`.
     - Push `(start, h)` onto the stack.
  2. After traversing the array, any remaining bars on the stack extend uninterrupted all the way to the right boundary of the histogram ($n = \text{len}(heights)$).
     - For each `(idx, h)` in `stack`, evaluate $\text{area} = h \times (n - \text{idx})$.
  3. Return the maximum area observed.

### Complexity:
- **Time Complexity:** $O(N)$ — Every bar is pushed and popped at most once in a single pass.
- **Space Complexity:** $O(N)$ — Stack stores at most $N$ elements.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # stores (start_index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_idx, prev_h = stack.pop()
                max_area = max(max_area, prev_h * (i - prev_idx))
                start = prev_idx

            stack.append((start, h))

        n = len(heights)
        for idx, h in stack:
            max_area = max(max_area, h * (n - idx))

        return max_area
```

---

## 🔑 Monotonic Stack Trace

```
heights = [2, 1, 5, 6, 2, 3]

i=0, h=2 : stack = [(0, 2)]
i=1, h=1 : 2 > 1 -> pop (0, 2) -> area = 2*(1-0) = 2; start = 0
           stack = [(0, 1)]
i=2, h=5 : stack = [(0, 1), (2, 5)]
i=3, h=6 : stack = [(0, 1), (2, 5), (3, 6)]
i=4, h=2 : 6 > 2 -> pop (3, 6) -> area = 6*(4-3) = 6; start = 3
           5 > 2 -> pop (2, 5) -> area = 5*(4-2) = 10 (Max!); start = 2
           stack = [(0, 1), (2, 2)]
i=5, h=3 : stack = [(0, 1), (2, 2), (5, 3)]

Right boundary flush (n=6):
pop (5, 3) -> area = 3*(6-5) = 3
pop (2, 2) -> area = 2*(6-2) = 8
pop (0, 1) -> area = 1*(6-0) = 6

Max Area = 10 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard LeetCode example (`[2, 1, 5, 6, 2, 3]` → `10`)
2. Two element simple case (`[2, 4]` → `4`)
3. Single bar histogram (`[5]` → `5`)
4. All zero heights (`[0, 0, 0]` → `0`)
5. Strictly increasing heights (`[1, 2, 3, 4, 5]` → `9`)
6. Strictly decreasing heights (`[5, 4, 3, 2, 1]` → `9`)
7. Uniform constant height bars (`[3, 3, 3, 3, 3]` → `15`)
8. Tall central spike (`[2, 1, 100, 1, 2]` → `100`)
9. Alternating heights (`[2, 1, 2]` → `3`)
10. Symmetrical valley (`[6, 1, 6]` → `6`)
