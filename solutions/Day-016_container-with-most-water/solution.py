"""
LeetCode #11: Container With Most Water
Difficulty: Medium
Topic: Two Pointers
Date Solved: 2026-10-07

Problem:
You are given an integer array `height` of length n. There are n vertical lines
drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.
Note: You may not slant the container.
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find the maximum water container area using Two Pointers — O(N) time.

        Intuition:
        The water area formed by lines at indices `left` and `right` is:
            area = min(height[left], height[right]) * (right - left)

        A brute-force O(N^2) approach checks every pair. We can do O(N) with
        the two-pointer greedy insight:

        Greedy Key Insight:
        Start with the widest container (left=0, right=n-1). To potentially
        increase the area, we must increase the height (since width decreases
        when we move pointers inward). The current area is limited by the
        SHORTER line. Moving the taller line inward can only decrease width
        while keeping the bottleneck the same → guaranteed to decrease area.
        Therefore, we should always move the pointer at the SHORTER line.

        Algorithm:
        1. left = 0, right = n-1, best = 0.
        2. While left < right:
            a. Compute area = min(height[left], height[right]) * (right - left).
            b. Update best = max(best, area).
            c. Move the pointer at the shorter line inward:
               - height[left] <= height[right] → left++
               - Otherwise → right--
        3. Return best.

        Proof of correctness:
        When we move the shorter-line pointer, we are not missing any better pair:
        - All pairs (left, x) for x < right have been or will be implicitly
          eliminated because min(height[left], height[x]) * (x - left) can never
          exceed the current area if height[left] is the bottleneck.

        Complexity:
        - Time Complexity: O(N) — left and right together traverse the array once.
        - Space Complexity: O(1) — only three integer variables.
        """
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            # Width = distance between lines; height = shorter of the two lines
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)

            # Move the pointer at the shorter line to search for a taller one
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return best


# --- Unit Tests ---
def test_max_area():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    assert solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "TC1 failed"

    # Test Case 2: LeetCode Example 2 — two elements
    assert solver.maxArea([1, 1]) == 1, "TC2 failed"

    # Test Case 3: Increasing heights — answer at rightmost pair
    assert solver.maxArea([1, 2, 3, 4, 5]) == 6, "TC3 failed"

    # Test Case 4: Decreasing heights — answer at leftmost pair
    assert solver.maxArea([5, 4, 3, 2, 1]) == 6, "TC4 failed"

    # Test Case 5: All equal heights
    assert solver.maxArea([3, 3, 3, 3]) == 9, "TC5 failed"

    # Test Case 6: Large values at both ends
    assert solver.maxArea([100, 1, 1, 100]) == 300, "TC6 failed"

    # Test Case 7: Peak in the middle — best pair is not adjacent
    assert solver.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24, "TC7 failed"

    # Test Case 8: Two tall lines with short lines in between
    assert solver.maxArea([9, 1, 1, 1, 1, 9]) == 45, "TC8 failed"

    # Test Case 9: Single tall line surrounded by short lines
    assert solver.maxArea([1, 5, 1, 5, 1]) == 10, "TC9 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_max_area()
