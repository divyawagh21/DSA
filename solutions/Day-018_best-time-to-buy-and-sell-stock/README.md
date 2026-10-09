# Day 18: Best Time to Buy and Sell Stock

- **Problem Link:** [LeetCode #121 - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- **Difficulty:** 🟢 Easy
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-09

---

## 📝 Problem Statement

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the **maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Example 1:
```text
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

### Example 2:
```text
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### Constraints:
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## 💡 Algorithmic Approaches

### 1. Brute Force (Nested Loops)
- Check every pair `(i, j)` where `j > i` and calculate `prices[j] - prices[i]`.
- **Time Complexity:** $O(N^2)$ — Exceeds time limit for $N = 10^5$.
- **Space Complexity:** $O(1)$.

### 2. Sliding Window / Single Pass (Optimal) 🚀
- Maintain two pointers / state variables:
  - `min_price`: The minimum buy price observed up to the current day.
  - `max_profit`: The highest profit achieved so far.
- As we iterate through each day's price:
  - If `price < min_price`: Update `min_price` (slide left window boundary forward to today).
  - Else: Calculate potential profit `price - min_price` and update `max_profit`.
- **Time Complexity:** $O(N)$ — Single pass through the array.
- **Space Complexity:** $O(1)$ — Only two scalar variables stored in memory.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit
```

---

## 🔑 Sliding Window Visualisation

```
prices = [ 7,   1,   5,   3,   6,   4 ]
           ▲    ▲
        min=7 min=1
                ▲ prof=4
                     ▲ prof=2
                          ▲ prof=5 (Max!)
                               ▲ prof=3

Best Transaction: Buy @ 1, Sell @ 6 → Profit = 5
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit test cases:
1. Standard volatile series with profitable peak (`[7, 1, 5, 3, 6, 4]` → `5`)
2. Monotonically decreasing series with no profitable opportunity (`[7, 6, 4, 3, 1]` → `0`)
3. Empty input list (`[]` → `0`)
4. Single-element price boundary condition (`[10]` → `0`)
5. Two elements ascending (`[1, 10]` → `9`)
6. Two elements descending (`[10, 1]` → `0`)
7. Constant prices with zero variance (`[5, 5, 5, 5]` → `0`)
8. Minimum price at final index after earlier peaks (`[3, 8, 2, 5, 1]` → `5`)
9. Earlier peak followed by deeper valley and higher peak (`[2, 4, 1, 7]` → `6`)
10. Multiple local extrema (`[3, 2, 6, 5, 0, 3]` → `4`)
