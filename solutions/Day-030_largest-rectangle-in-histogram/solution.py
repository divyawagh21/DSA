"""
LeetCode #84: Largest Rectangle in Histogram
Difficulty: Hard
Topic: Stack
Date Solved: 2026-10-18

Problem:
Given an array of integers `heights` representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Find the maximum rectangular area in a histogram using a Monotonic Increasing Stack.

        Intuition:
        For each bar of height `h`, we want to find how far it can extend horizontally to the
        left and to the right before hitting a bar shorter than itself.
        A naive brute-force checks all pairs in O(N^2), which times out for N = 10^5.

        Monotonic Stack Insight:
        We maintain a stack of `(index, height)` tuples in strictly non-decreasing order of heights.
        
        1. As we iterate through each bar `(i, h)`:
           - If `h` is smaller than the height at the top of the stack, the taller bar on the stack
             CANNOT extend past index `i` to the right.
           - We pop `(prev_idx, prev_h)` and compute its rectangle area:
             `area = prev_h * (i - prev_idx)`.
           - Crucial: The current shorter bar `h` CAN extend backwards to `prev_idx` because the
             popped bar was taller than `h`! Thus, we update the starting index of the current bar
             to `prev_idx`.
           - Push `(start_idx, h)` onto the stack.

        2. After processing all bars, any remaining bars on the stack can extend all the way to
           the end of the histogram (`n = len(heights)`).
           We pop each `(idx, h)` and compute `area = h * (n - idx)`.

        Complexity:
        - Time Complexity: O(N) — Every bar is pushed and popped at most once.
        - Space Complexity: O(N) — In the worst case (strictly increasing heights), the stack stores N pairs.
        """
        max_area = 0
        stack = []  # pairs: (index, height)

        for i, h in enumerate(heights):
            start = i
            # Pop taller bars that cannot extend past index i
            while stack and stack[-1][1] > h:
                prev_idx, prev_h = stack.pop()
                area = prev_h * (i - prev_idx)
                if area > max_area:
                    max_area = area
                start = prev_idx  # current bar h extends back to prev_idx

            stack.append((start, h))

        # Process any remaining bars that extend to the right boundary
        n = len(heights)
        for idx, h in stack:
            area = h * (n - idx)
            if area > max_area:
                max_area = area

        return max_area


# --- Unit Tests ---
def test_largest_rectangle_area():
    solver = Solution()

    # Test Case 1: Standard case from LeetCode
    assert solver.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10, "TC1 failed"

    # Test Case 2: Two elements
    assert solver.largestRectangleArea([2, 4]) == 4, "TC2 failed"

    # Test Case 3: Single bar
    assert solver.largestRectangleArea([5]) == 5, "TC3 failed"

    # Test Case 4: All zero heights
    assert solver.largestRectangleArea([0, 0, 0]) == 0, "TC4 failed"

    # Test Case 5: Strictly increasing heights
    # [1, 2, 3, 4, 5] -> rectangles: 5*1=5, 4*2=8, 3*3=9, 2*4=8, 1*5=5 -> max=9
    assert solver.largestRectangleArea([1, 2, 3, 4, 5]) == 9, "TC5 failed"

    # Test Case 6: Strictly decreasing heights
    # [5, 4, 3, 2, 1] -> max=9
    assert solver.largestRectangleArea([5, 4, 3, 2, 1]) == 9, "TC6 failed"

    # Test Case 7: Uniform constant heights
    assert solver.largestRectangleArea([3, 3, 3, 3, 3]) == 15, "TC7 failed"

    # Test Case 8: Tall spike in the middle
    assert solver.largestRectangleArea([2, 1, 100, 1, 2]) == 100, "TC8 failed"

    # Test Case 9: Alternating heights
    # [2, 1, 2] -> max is 3 (1*3)
    assert solver.largestRectangleArea([2, 1, 2]) == 3, "TC9 failed"

    # Test Case 10: Valley with high walls
    # [6, 1, 6] -> max is 6 (6*1)
    assert solver.largestRectangleArea([6, 1, 6]) == 6, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_largest_rectangle_area()
