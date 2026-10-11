# Day 23: Sliding Window Maximum

- **Problem Link:** [LeetCode #239 - Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- **Difficulty:** 🔴 Hard
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-11

---

## 📝 Problem Statement

You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the **max sliding window**.

### Example 1:
```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Example 2:
```text
Input: nums = [1], k = 1
Output: [1]
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- For every window starting at index $i$, scan $k$ elements to find the maximum: $\max(nums[i:i+k])$.
- **Time Complexity:** $O((N - k + 1) \cdot k) = O(N \cdot k)$ — Exceeds the time limit for $N, k = 10^5$ ($10^{10}$ operations).
- **Space Complexity:** $O(1)$.

### 2. Max-Heap / Priority Queue
- Keep a heap of `(-val, index)` pairs. For each step, pop stale roots where `index <= i - k`.
- **Time Complexity:** $O(N \log N)$ or $O(N \log k)$ — Reasonable, but heap rebalancing incurs extra overhead.
- **Space Complexity:** $O(N)$ or $O(k)$.

### 3. Monotonic Decreasing Deque (Optimal) 🚀
- Use a double-ended queue (`collections.deque`) to store **indices**.
- Elements in the deque are maintained in strictly **decreasing order** of values:
  `nums[deque[0]] > nums[deque[1]] > ... > nums[deque[-1]]`
- **Why this works:**
  1. If a new element $nums[i]$ is larger than or equal to elements currently in the deque, those smaller elements can **never** be the maximum of this or any future window because $nums[i]$ is both larger and will persist longer in future windows! We safely pop them from the back.
  2. The element at the front `deque[0]` is **always the maximum** of the current window.
  3. When `deque[0] <= i - k`, it has left the current window boundary, so we pop it from the front.
- **Time Complexity:** $O(N)$ — Every index is pushed onto the deque once and popped at most once.
- **Space Complexity:** $O(k)$ — Deque stores at most $k$ indices at any point.

---

## 💻 Python Implementation

```python
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        if k == 1:
            return nums

        dq = deque()
        result = []

        for i, val in enumerate(nums):
            # 1. Pop element if outside window boundary
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain monotonic decreasing deque order
            while dq and nums[dq[-1]] <= val:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Record maximum when window is of size k
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
```

---

## 🔑 Monotonic Deque Trace

```
nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

i=0, val=1  : dq=[0 (val 1)]
i=1, val=3  : 3 > 1 -> pop 0 -> dq=[1 (val 3)]
i=2, val=-1 : dq=[1, 2 (vals 3, -1)]               -> Window 1 Max = 3
i=3, val=-3 : dq=[1, 2, 3 (vals 3, -1, -3)]        -> Window 2 Max = 3
i=4, val=5  : pop 1 (out of win), pop 3, 2 (5 > -1,-3) -> dq=[4 (val 5)] -> Window 3 Max = 5
i=5, val=3  : dq=[4, 5 (vals 5, 3)]                -> Window 4 Max = 5
i=6, val=6  : pop 5, 4 (6 > 5, 3) -> dq=[6 (val 6)] -> Window 5 Max = 6
i=7, val=7  : pop 6 (7 > 6) -> dq=[7 (val 7)]       -> Window 6 Max = 7

Result: [3, 3, 5, 5, 6, 7] ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard problem example with negative numbers (`[1, 3, -1, -3, 5, 3, 6, 7]`, k=3 → `[3, 3, 5, 5, 6, 7]`)
2. Single-element array with $k=1$ (`[1]`, k=1 → `[1]`)
3. Strictly decreasing array (`[9, 8, 7, 6, 5, 4]`, k=3 → `[9, 8, 7, 6]`)
4. Strictly increasing array (`[1, 2, 3, 4, 5, 6]`, k=3 → `[3, 4, 5, 6]`)
5. Window size $k$ equals array length (`[4, 2, 7, 1, 9]`, k=5 → `[9]`)
6. Window size $k=1$ (`[2, 1, 5, 3]`, k=1 → `[2, 1, 5, 3]`)
7. All identical elements (`[5, 5, 5, 5, 5]`, k=2 → `[5, 5, 5, 5]`)
8. Large window with negative and positive values (`[-7, -8, -7, 5, 7, 1, 6, 0]`, k=4 → `[5, 7, 7, 7, 7]`)
9. Alternating peaks and troughs (`[1, 3, 1, 2, 0, 5]`, k=3 → `[3, 3, 2, 5]`)
10. Two-element array (`[1, -1]`, k=1 → `[1, -1]`)
