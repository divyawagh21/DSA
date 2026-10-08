"""
LeetCode #42: Trapping Rain Water
Difficulty: Hard
Topic: Two Pointers
Date Solved: 2026-10-08

Problem:
Given `n` non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculates trapped rainwater using the Two Pointers technique — O(N) time, O(1) space.

        Intuition & Mathematical Foundation:
        At any index `i`, the water level above bar `i` is determined entirely by:
            water[i] = max(0, min(max_left[i], max_right[i]) - height[i])

        A classic DP approach precomputes prefix maximums (left_max) and suffix
        maximums (right_max) using O(N) time and O(N) auxiliary space.

        Optimal Two-Pointer Reduction:
        Notice we don't actually need the exact value of both maximums at every step.
        We only need to know WHICH side has the smaller maximum (the bottleneck):
        - If `left_max < right_max`, the water trapped at `left` is guaranteed to be
          governed by `left_max` because the boundary on the right is at least `right_max`,
          which is strictly greater. Whatever happens in between cannot lower the right wall below `right_max`.
        - Conversely, if `right_max <= left_max`, the bottleneck for `right` is guaranteed
          to be `right_max`.

        Algorithm:
        1. If len(height) < 3, return 0 (no container can be formed).
        2. Initialize two pointers: `left = 0`, `right = len(height) - 1`.
        3. Maintain running maximums: `left_max = height[left]`, `right_max = height[right]`.
        4. While `left < right`:
            - If `left_max < right_max`:
                a. Advance `left += 1`.
                b. Update `left_max = max(left_max, height[left])`.
                c. Accumulate `water += left_max - height[left]`.
            - Else:
                a. Advance `right -= 1`.
                b. Update `right_max = max(right_max, height[right])`.
                c. Accumulate `water += right_max - height[right]`.
        5. Return accumulated `water`.

        Complexity:
        - Time Complexity: O(N) — Each index is visited exactly once as left and right converge.
        - Space Complexity: O(1) — Constant extra space (four pointer/accumulator variables).
        """
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water

    def trap_dp(self, height: List[int]) -> int:
        """
        Alternative: Dynamic Programming (Prefix & Suffix Max) — O(N) time, O(N) space.
        Used for verification and cross-checking correctness against the two-pointer approach.
        """
        n = len(height)
        if n < 3:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            bottleneck = min(left_max[i], right_max[i])
            if bottleneck > height[i]:
                total_water += bottleneck - height[i]

        return total_water


# --- Unit Tests ---
def test_trap():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    # [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
    tc1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert solver.trap(tc1) == 6, f"TC1 failed: {solver.trap(tc1)}"
    assert solver.trap_dp(tc1) == 6, "TC1 DP failed"

    # Test Case 2: LeetCode Example 2
    # [4,2,0,3,2,5] -> 9
    tc2 = [4, 2, 0, 3, 2, 5]
    assert solver.trap(tc2) == 9, f"TC2 failed: {solver.trap(tc2)}"
    assert solver.trap_dp(tc2) == 9, "TC2 DP failed"

    # Test Case 3: Empty array and small inputs (< 3 elements cannot trap water)
    assert solver.trap([]) == 0, "TC3 empty failed"
    assert solver.trap([5]) == 0, "TC3 single failed"
    assert solver.trap([3, 4]) == 0, "TC3 pair failed"

    # Test Case 4: Strictly increasing heights (water spills off left)
    tc4 = [1, 2, 3, 4, 5]
    assert solver.trap(tc4) == 0, f"TC4 failed: {solver.trap(tc4)}"

    # Test Case 5: Strictly decreasing heights (water spills off right)
    tc5 = [5, 4, 3, 2, 1]
    assert solver.trap(tc5) == 0, f"TC5 failed: {solver.trap(tc5)}"

    # Test Case 6: Flat / all equal elevations
    tc6 = [3, 3, 3, 3]
    assert solver.trap(tc6) == 0, f"TC6 failed: {solver.trap(tc6)}"

    # Test Case 7: Simple single symmetrical valley
    # [3, 0, 3] -> 3 units
    tc7 = [3, 0, 3]
    assert solver.trap(tc7) == 3, f"TC7 failed: {solver.trap(tc7)}"

    # Test Case 8: Deep wide trench
    # [5, 1, 1, 1, 5] -> (5-1)*3 = 12
    tc8 = [5, 1, 1, 1, 5]
    assert solver.trap(tc8) == 12, f"TC8 failed: {solver.trap(tc8)}"

    # Test Case 9: Asymmetric container with inner steps
    # [4, 2, 3] -> 1 unit trapped above index 1
    tc9 = [4, 2, 3]
    assert solver.trap(tc9) == 1, f"TC9 failed: {solver.trap(tc9)}"

    # Test Case 10: Multi-basin landscape with varied heights
    # [5, 2, 1, 2, 1, 5]
    # left_max=5, right_max=5 -> (5-2)+(5-1)+(5-2)+(5-1) = 3 + 4 + 3 + 4 = 14
    tc10 = [5, 2, 1, 2, 1, 5]
    assert solver.trap(tc10) == 14, f"TC10 failed: {solver.trap(tc10)}"
    assert solver.trap_dp(tc10) == 14, "TC10 DP failed"

    # Test Case 11: Zeros with tall boundary walls
    tc11 = [10, 0, 0, 10]
    assert solver.trap(tc11) == 20, f"TC11 failed: {solver.trap(tc11)}"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_trap()
