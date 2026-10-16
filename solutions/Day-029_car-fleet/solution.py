"""
LeetCode #853: Car Fleet
Difficulty: Medium
Topic: Stack
Date Solved: 2026-10-16

Problem:
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer array `position` and `speed`, both of length n, where `position[i]`
is the starting position of the i-th car and `speed[i]` is the speed of the i-th car.

A car cannot pass another car ahead of it, but it can catch up to it and drive bumper to bumper
at the same speed. If a car catches up to a car fleet right at the destination point, it is still
considered as one car fleet.

Return the number of car fleets that will arrive at the destination.
"""

from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Determine the number of car fleets arriving at target using Sort + Monotonic Stack.

        Intuition:
        Cars cannot pass one another. Therefore, whether a car catches up to the car
        ahead depends solely on its arrival time to the destination target:
            time_to_target = (target - position) / speed

        Key Insight:
        If we process cars from right to left (closest to the destination first):
        - A car behind another car will catch up if its unconstrained time to reach target
          is LESS THAN OR EQUAL TO the time of the fleet in front of it.
        - Because it cannot overtake, it will be slowed down to the front fleet's speed and
          merge into that existing fleet.
        - If its time is GREATER, it can never catch up before reaching the target, and thus
          originates a new distinct fleet.

        Algorithm:
        1. Pair each position with its speed and sort in descending order of position.
        2. Maintain a stack of fleet arrival times.
        3. For each car:
           - Calculate `time = (target - pos) / spd`.
           - If `stack` has a fleet and `time <= stack[-1]`, this car joins the fleet ahead
             (no new fleet created).
           - Otherwise, this car is slower and forms a new fleet: `stack.append(time)`.
        4. The number of fleets equals `len(stack)`.

        Complexity:
        - Time Complexity: O(N log N) — Dominated by sorting N cars by starting position.
          The subsequent stack scan runs in linear O(N) time.
        - Space Complexity: O(N) — Storage for the paired tuples and arrival time stack.
        """
        pair = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack = []

        for pos, spd in pair:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


# --- Unit Tests ---
def test_car_fleet():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    # Target = 12, pos = [10, 8, 0, 5, 3], speed = [2, 4, 1, 1, 3]
    # Cars sorted:
    # (10, 2) -> time = 1.0 (Fleet 1)
    # (8, 4)  -> time = 1.0 <= 1.0 -> merges into Fleet 1
    # (5, 1)  -> time = 7.0 > 1.0  -> (Fleet 2)
    # (3, 3)  -> time = 3.0 <= 7.0 -> merges into Fleet 2
    # (0, 1)  -> time = 12.0 > 7.0 -> (Fleet 3)
    # Result: 3 fleets
    assert solver.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3, "TC1 failed"

    # Test Case 2: Single car
    assert solver.carFleet(10, [3], [3]) == 1, "TC2 failed on single car"

    # Test Case 3: Two cars, second catches up at target
    # pos=[0, 2], speed=[4, 2], target=100
    # car at 2: time = (100 - 2) / 2 = 49
    # car at 0: time = (100 - 0) / 4 = 25 <= 49 -> 1 fleet
    assert solver.carFleet(100, [0, 2], [4, 2]) == 1, "TC3 failed"

    # Test Case 4: All cars arrive at different times (no catchup)
    # pos=[0, 2, 4], speed=[1, 1, 1], target=10
    # times = [10, 8, 6] -> 3 distinct fleets
    assert solver.carFleet(10, [0, 2, 4], [1, 1, 1]) == 3, "TC4 failed"

    # Test Case 5: Faster car already ahead (can never be caught)
    # pos=[0, 4], speed=[1, 2], target=10
    # car at 4: time = 6 / 2 = 3
    # car at 0: time = 10 / 1 = 10 > 3 -> 2 fleets
    assert solver.carFleet(10, [0, 4], [1, 2]) == 2, "TC5 failed"

    # Test Case 6: Exact tie at destination
    # pos=[0, 5], speed=[10, 5], target=10
    # car at 5: time = 5 / 5 = 1.0
    # car at 0: time = 10 / 10 = 1.0 -> same time at target -> 1 fleet
    assert solver.carFleet(10, [0, 5], [10, 5]) == 1, "TC6 failed"

    # Test Case 7: Chain of cars cascading into one fleet
    # pos=[0, 2, 4, 6], speed=[4, 3, 2, 1], target=10
    # times: (6): 4/1=4; (4): 6/2=3<=4; (2): 8/3=2.67<=4; (0): 10/4=2.5<=4 -> 1 fleet
    assert solver.carFleet(10, [0, 2, 4, 6], [4, 3, 2, 1]) == 1, "TC7 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_car_fleet()
