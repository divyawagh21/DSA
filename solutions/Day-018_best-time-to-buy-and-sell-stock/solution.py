"""
LeetCode #121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Sliding Window
Date Solved: 2026-10-09

Problem:
You are given an array `prices` where `prices[i]` is the price of a given stock
on the i-th day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate maximum single-transaction profit using a Sliding Window / Single Pass.

        Intuition:
        To maximize profit = (sell_price - buy_price), we need to buy at the lowest
        possible price before selling at the highest future price.
        
        Using a sliding window concept:
        - The left boundary (`min_price`) represents our best historical buy day.
        - The right boundary scans each day as a candidate sell day.
        - If today's price is cheaper than `min_price`, we slide our buy window forward
          to today because any future sale will yield a better profit using today's price.
        - Otherwise, we calculate current profit = `price - min_price` and record
          the global maximum profit.

        Complexity:
        - Time Complexity: O(N) — Single linear scan through prices array.
        - Space Complexity: O(1) — Constant extra space for two variables.
        """
        if not prices:
            return 0

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


# --- Unit Tests ---
def test_max_profit():
    solver = Solution()

    # Test Case 1: Standard profitable case
    assert solver.maxProfit([7, 1, 5, 3, 6, 4]) == 5, "TC1 failed (Buy day 2 @1, sell day 5 @6)"

    # Test Case 2: Strictly decreasing prices — no profit possible
    assert solver.maxProfit([7, 6, 4, 3, 1]) == 0, "TC2 failed (Descending prices)"

    # Test Case 3: Empty prices list
    assert solver.maxProfit([]) == 0, "TC3 failed (Empty list)"

    # Test Case 4: Single element array — cannot buy and sell on distinct days
    assert solver.maxProfit([10]) == 0, "TC4 failed (Single price)"

    # Test Case 5: Two elements — profitable
    assert solver.maxProfit([1, 10]) == 9, "TC5 failed (Simple pair)"

    # Test Case 6: Two elements — loss
    assert solver.maxProfit([10, 1]) == 0, "TC6 failed (Pair loss)"

    # Test Case 7: Flat prices (no change)
    assert solver.maxProfit([5, 5, 5, 5]) == 0, "TC7 failed (Flat prices)"

    # Test Case 8: Lowest price occurs on the very last day
    assert solver.maxProfit([3, 8, 2, 5, 1]) == 5, "TC8 failed (Min on last day)"

    # Test Case 9: Large peak followed by new lower dip and moderate rise
    assert solver.maxProfit([2, 4, 1, 7]) == 6, "TC9 failed (Buy @1, sell @7)"

    # Test Case 10: Volatile stock with multiple local peaks
    assert solver.maxProfit([3, 2, 6, 5, 0, 3]) == 4, "TC10 failed (Buy @2, sell @6)"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_max_profit()
