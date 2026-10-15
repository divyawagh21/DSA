"""
LeetCode #739: Daily Temperatures
Difficulty: Medium
Topic: Stack
Date Solved: 2026-10-15

Problem:
Given an array of integers `temperatures` represents the daily temperatures,
return an array `answer` such that `answer[i]` is the number of days you have to wait
after the i-th day to get a warmer temperature. If there is no future day for which
this is possible, keep `answer[i] == 0` instead.
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Find the number of days until a warmer temperature using a Monotonic Decreasing Stack.

        Intuition:
        For each day `i`, we need the distance to the first future day `j > i` with
        `temperatures[j] > temperatures[i]`.
        A brute force search takes O(N^2), which times out for N = 10^5.

        Instead, we use a Monotonic Decreasing Stack to store unresolved INDICES:
        - The stack maintains temperatures in strictly non-increasing order:
          temperatures[stack[0]] >= temperatures[stack[1]] >= ...
        - When we observe a day with temperature `temp`:
          - If `temp` is warmer than the temperature at the index on top of the stack,
            we have found the nearest warmer day for `prev_idx = stack.pop()`!
            We resolve it: `answer[prev_idx] = current_idx - prev_idx`.
          - Repeat until the stack top is warmer than or equal to `temp`.
          - Push `current_idx` onto the stack.
        - Any indices remaining on the stack at the end have no warmer future day and remain 0.

        Complexity:
        - Time Complexity: O(N) — Every index is pushed and popped from the stack at most once.
        - Space Complexity: O(N) — In the worst case (strictly decreasing temperatures),
          the stack holds all N indices.
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Stores indices of temperatures in monotonic decreasing order

        for curr_idx, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = curr_idx - prev_idx

            stack.append(curr_idx)

        return answer


# --- Unit Tests ---
def test_daily_temperatures():
    solver = Solution()

    # Test Case 1: Standard case from LeetCode
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solver.dailyTemperatures(temps1) == expected1, "TC1 failed"

    # Test Case 2: Consecutive increasing temperatures
    temps2 = [30, 40, 50, 60]
    expected2 = [1, 1, 1, 0]
    assert solver.dailyTemperatures(temps2) == expected2, "TC2 failed"

    # Test Case 3: Strictly decreasing temperatures (no warmer day exists)
    temps3 = [30, 60, 90]
    expected3 = [1, 1, 0]
    assert solver.dailyTemperatures(temps3) == expected3, "TC3 failed"

    # Test Case 4: Strictly descending array
    temps4 = [80, 70, 60, 50]
    expected4 = [0, 0, 0, 0]
    assert solver.dailyTemperatures(temps4) == expected4, "TC4 failed"

    # Test Case 5: Single element array
    temps5 = [45]
    expected5 = [0]
    assert solver.dailyTemperatures(temps5) == expected5, "TC5 failed"

    # Test Case 6: All identical temperatures
    temps6 = [50, 50, 50, 50]
    expected6 = [0, 0, 0, 0]
    assert solver.dailyTemperatures(temps6) == expected6, "TC6 failed"

    # Test Case 7: High temperature in middle followed by small dip
    temps7 = [60, 75, 70, 65, 80]
    expected7 = [1, 3, 2, 1, 0]
    assert solver.dailyTemperatures(temps7) == expected7, "TC7 failed"

    # Test Case 8: Two element array
    temps8 = [30, 31]
    expected8 = [1, 0]
    assert solver.dailyTemperatures(temps8) == expected8, "TC8 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_daily_temperatures()
