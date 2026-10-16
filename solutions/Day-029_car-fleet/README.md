# Day 29: Car Fleet

- **Problem Link:** [LeetCode #853 - Car Fleet](https://leetcode.com/problems/car-fleet/)
- **Difficulty:** 🟡 Medium
- **Topic:** Stack
- **Date Solved:** 2026-10-16

---

## 📝 Problem Statement

There are `n` cars at given miles away from the starting mile `0`, traveling to reach the mile `target`.

You are given two integer arrays `position` and `speed`, both of length `n`, where `position[i]` is the starting position of the $i$-th car and `speed[i]` is the speed of the $i$-th car in miles per hour.

**Rules:**
- A car cannot pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed.
- The faster car slows down to match the slower car's speed.
- If a car catches up to a car fleet right at the destination point, it is still considered as one car fleet.

Return the **number of car fleets** that will arrive at the destination.

### Example 1:
```text
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
- Car at 10 (speed 2) arrives in (12-10)/2 = 1.0 hour.
- Car at 8 (speed 4) arrives in (12-8)/4 = 1.0 hour. Catches up to car ahead -> 1 fleet.
- Car at 5 (speed 1) arrives in (12-5)/1 = 7.0 hours -> New fleet.
- Car at 3 (speed 3) arrives in (12-3)/3 = 3.0 hours <= 7.0 hours -> Catches up to car ahead.
- Car at 0 (speed 1) arrives in (12-0)/1 = 12.0 hours > 7.0 hours -> New fleet.
Total fleets = 3.
```

### Example 2:
```text
Input: target = 10, position = [3], speed = [3]
Output: 1
```

### Example 3:
```text
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
```

### Constraints:
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- All values of `position` are unique.
- `0 < speed[i] <= 10^6`

---

## 💡 Algorithmic Approaches

### 1. Simulation (Step by Step)
- Increment time in discrete intervals and simulate car movements.
- **Flaws:** Very slow when target is large ($10^6$) and speeds are small. Inexact for non-integer collision timestamps.
- **Time Complexity:** $O(target \cdot n)$ — Will encounter Time Limit Exceeded.

### 2. Sort + Monotonic Stack (Optimal) 🚀
- **Key Insight:** Whether car $B$ (behind) merges into car $A$ (ahead) depends on their calculated arrival times:
  $$\text{time} = \frac{\text{target} - \text{position}}{\text{speed}}$$
- If $\text{time}_B \le \text{time}_A$, car $B$ will inevitably catch up to car $A$ before or at `target`. Since car $B$ cannot pass, it merges into car $A$'s fleet and adopts car $A$'s arrival time.
- If $\text{time}_B > \text{time}_A$, car $B$ is slower and will never catch up to car $A$, forming the head of a **new fleet**.
- **Algorithm:**
  1. Pair each car's position with its speed and sort in descending order of position (closest to destination first).
  2. Maintain a stack of fleet arrival times.
  3. For each car:
     - Compute $\text{time} = (\text{target} - \text{pos}) / \text{spd}$.
     - If `stack` is non-empty and $\text{time} \le \text{stack}[-1]$, it joins the fleet ahead.
     - Else, it starts a new fleet: `stack.append(time)`.
  4. Return `len(stack)`.

### Complexity:
- **Time Complexity:** $O(N \log N)$ — Dominated by sorting $N$ cars. The subsequent linear scan is $O(N)$.
- **Space Complexity:** $O(N)$ — For storing sorted pairs and the arrival time stack.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []

        for pos, spd in pair:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)
```

---

## 🔑 Car Fleet Arrival Trace

```
target = 12
position = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]

Sort by position desc:
(10, 2) -> time = 1.0  -> stack = [1.0]           (Fleet 1)
(8, 4)  -> time = 1.0  -> 1.0 <= 1.0 -> merges!   (Fleet 1)
(5, 1)  -> time = 7.0  -> 7.0 > 1.0  -> stack = [1.0, 7.0]  (Fleet 2)
(3, 3)  -> time = 3.0  -> 3.0 <= 7.0 -> merges!   (Fleet 2)
(0, 1)  -> time = 12.0 -> 12.0 > 7.0 -> stack = [1.0, 7.0, 12.0] (Fleet 3)

Total Fleets: 3 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 7 automated unit tests:
1. Standard multi-fleet case from LeetCode (`target=12`, 5 cars → `3`)
2. Single car boundary condition (`target=10`, 1 car → `1`)
3. Catching up right at the destination point (`target=100`, 2 cars → `1`)
4. Distinct speeds with no overlap (`times = [10, 8, 6]` → `3`)
5. Faster car ahead with slower car behind (`times = [3, 10]` → `2`)
6. Exact arrival time tie at destination (`times = [1.0, 1.0]` → `1`)
7. Cascading fleet where all cars merge into the slowest frontrunner (`4 cars` → `1`)
