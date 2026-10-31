# Day 33: Koko Eating Bananas

- **Problem Link:** [LeetCode #875 - Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- **Difficulty:** 🟡 Medium
- **Topic:** Binary Search
- **Date Solved:** 2026-10-31

---

## 📝 Problem Statement

Koko loves to eat bananas. There are `n` piles of bananas, the $i$-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the **minimum integer `k`** such that she can eat all the bananas within `h` hours.

### Example 1:
```text
Input: piles = [3,6,7,11], h = 8
Output: 4
Explanation:
- At speed 4:
  - Pile 3: ceil(3/4) = 1 hour
  - Pile 6: ceil(6/4) = 2 hours
  - Pile 7: ceil(7/4) = 2 hours
  - Pile 11: ceil(11/4) = 3 hours
  Total hours = 1 + 2 + 2 + 3 = 8 <= 8
```

### Example 2:
```text
Input: piles = [30,11,23,4,20], h = 5
Output: 30
Explanation: Since h == len(piles), Koko must finish each pile in at most 1 hour, so k = max(piles) = 30.
```

### Example 3:
```text
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

### Constraints:
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

---

## 💡 Algorithmic Approaches

### 1. Linear Scan from $k = 1$ to $\max(\text{piles})$ (Brute Force)
- Test each eating speed $k = 1, 2, 3, \dots$ until total hours $\le h$.
- **Time Complexity:** $O(\max(\text{piles}) \times N)$ — Infeasible when $\max(\text{piles}) = 10^9$ ($10^{13}$ operations).
- **Space Complexity:** $O(1)$.

### 2. Binary Search on the Answer (Optimal) 🚀
- **Monotonic Feasibility Property:**
  - Notice the monotonic relationship: if speed $k$ is fast enough to finish within $h$ hours, any speed $k' > k$ is also fast enough.
  - If speed $k$ is too slow, any speed $k' < k$ is also guaranteed to be too slow.
  - This monotonic predicate allows us to binary search the eating speed $k$ directly over $[1, \max(\text{piles})]$.

- **Hours Formula:**
  - For pile $p$ eaten at rate $k$, hours taken is $\lceil p / k \rceil = (p + k - 1) // k$.
  - Total time = $\sum_{p \in \text{piles}} \lceil p / k \rceil$.

- **Algorithm:**
  1. Set search range: $\text{left} = 1$, $\text{right} = \max(\text{piles})$.
  2. While $\text{left} \le \text{right}$:
     - $\text{mid} = \text{left} + (\text{right} - \text{left}) // 2$.
     - Compute $\text{hours} = \sum \lceil p / \text{mid} \rceil$.
     - If $\text{hours} \le h$: record $\text{ans} = \text{mid}$ and search left half ($\text{right} = \text{mid} - 1$) to find smaller speeds.
     - If $\text{hours} > h$: search right half ($\text{left} = \text{mid} + 1$).
  3. Return $\text{ans}$.

### Complexity:
- **Time Complexity:** $O(N \log(\max(\text{piles})))$ — At most $\log_2(10^9) \approx 30$ iterations. Each iteration takes $O(N)$ to calculate total hours. Total operations $\approx 30 \times 10^4 = 3 \times 10^5$, executing in a few milliseconds!
- **Space Complexity:** $O(1)$ — Only scalar loop variables are stored.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2

            hours_needed = 0
            for p in piles:
                hours_needed += (p + mid - 1) // mid

            if hours_needed <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
```

---

## 🔑 Binary Search on Answer Trace

```
piles = [3, 6, 7, 11], h = 8
Search space: left = 1, right = 11

Iter 1: mid = 6 -> hours = 1 + 1 + 2 + 2 = 6 <= 8 (Valid) -> ans = 6, right = 5
Iter 2: mid = 3 -> hours = 1 + 2 + 3 + 4 = 10 > 8 (Too slow) -> left = 4
Iter 3: mid = 4 -> hours = 1 + 2 + 2 + 3 = 8 <= 8 (Valid) -> ans = 4, right = 3
Iter 4: left = 4, right = 3 -> loop terminates!

Final minimum speed = 4 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard LeetCode example (`[3, 6, 7, 11]`, $h = 8$ → `4`)
2. Tight boundary $h == \text{len}(\text{piles})$ (`[30, 11, 23, 4, 20]`, $h = 5$ → `30`)
3. Standard intermediate example (`[30, 11, 23, 4, 20]`, $h = 6$ → `23`)
4. Single pile with $h > 1$ (`[10]`, $h = 2$ → `5`)
5. Single pile with $h == \text{pile}$ (`[10]`, $h = 10$ → `1`)
6. Generous time $h \gg \sum \text{piles}$ (`[1, 1, 1, 1]`, $h = 100$ → `1`)
7. Equal pile sizes with $h == \text{len}(\text{piles})$ (`[5, 5, 5, 5]`, $h = 4$ → `5`)
8. Equal pile sizes with $h == 2 \times \text{len}(\text{piles})$ (`[5, 5, 5, 5]`, $h = 8$ → `3`)
9. Maximum constraint value $10^9$ (`[1000000000]`, $h = 2$ → `500000000`)
10. Large values with non-trivial ceil division (`[312884470]`, $h = 968709470$ → `1`)
