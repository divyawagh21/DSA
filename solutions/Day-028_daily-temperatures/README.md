# Day 28: Daily Temperatures

- **Problem Link:** [LeetCode #739 - Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
- **Difficulty:** 🟡 Medium
- **Topic:** Stack
- **Date Solved:** 2026-10-15

---

## 📝 Problem Statement

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

### Example 1:
```text
Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
```

### Example 2:
```text
Input:  temperatures = [30, 40, 50, 60]
Output: [1, 1, 1, 0]
```

### Example 3:
```text
Input:  temperatures = [30, 60, 90]
Output: [1, 1, 0]
```

### Constraints:
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- For each day $i$, scan all future days $j > i$ to find the first index where $\text{temperatures}[j] > \text{temperatures}[i]$.
- **Time Complexity:** $O(N^2)$ — Times out for $N = 10^5$.
- **Space Complexity:** $O(1)$.

### 2. Monotonic Decreasing Stack (Optimal) 🚀
- **Key Insight:** Maintain a stack of unresolved days' indices. Keep the temperatures corresponding to these indices in strictly descending order.
- When evaluating the current day $(i, \text{temp})$:
  - While the stack is non-empty and $\text{temp} > \text{temperatures}[\text{stack}[-1]]$:
    - We have found the closest warmer day for $\text{prev\_idx} = \text{stack.pop()}$!
    - Calculate $\text{answer}[\text{prev\_idx}] = i - \text{prev\_idx}$.
  - Push $i$ onto the stack.
- Any days remaining on the stack at the end have no warmer future day and naturally stay $0$.

### Complexity:
- **Time Complexity:** $O(N)$ — Every index enters the stack once and leaves the stack at most once.
- **Space Complexity:** $O(N)$ — The stack stores at most $N$ elements.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # indices of monotonic decreasing temperatures

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = curr_idx - prev_idx

            stack.append(curr_idx)

        return answer
```

---

## 🔑 Monotonic Decreasing Stack Trace

```
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

i=0, temp=73 : stack=[0]
i=1, temp=74 : 74 > 73 -> pop 0 -> ans[0] = 1-0 = 1; stack=[1]
i=2, temp=75 : 75 > 74 -> pop 1 -> ans[1] = 2-1 = 1; stack=[2]
i=3, temp=71 : 71 <= 75 -> stack=[2, 3]
i=4, temp=69 : 69 <= 71 -> stack=[2, 3, 4]
i=5, temp=72 : 72 > 69 -> pop 4 -> ans[4] = 5-4 = 1
               72 > 71 -> pop 3 -> ans[3] = 5-3 = 2
               72 <= 75 -> stack=[2, 5]
i=6, temp=76 : 76 > 72 -> pop 5 -> ans[5] = 6-5 = 1
               76 > 75 -> pop 2 -> ans[2] = 6-2 = 4; stack=[6]
i=7, temp=73 : 73 <= 76 -> stack=[6, 7]

Final answer: [1, 1, 4, 2, 1, 1, 0, 0] ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 8 automated unit tests:
1. Standard oscillating pattern with multi-day waits (`[73, 74, 75, 71, 69, 72, 76, 73]`)
2. Strictly increasing daily temperatures (`[30, 40, 50, 60]`)
3. Steeply increasing step series (`[30, 60, 90]`)
4. Strictly descending array where no warmer days exist (`[80, 70, 60, 50]`)
5. Single day boundary case (`[45]`)
6. Flat unchanging temperatures (`[50, 50, 50, 50]`)
7. Central peak followed by delayed recovery (`[60, 75, 70, 65, 80]`)
8. Minimal two-day comparison (`[30, 31]`)
