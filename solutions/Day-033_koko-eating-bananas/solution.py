"""
LeetCode #875: Koko Eating Bananas
Difficulty: Medium
Topic: Binary Search
Date Solved: 2026-10-31

Problem:
Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas.
The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas
and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them
instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.
"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum eating speed k using Binary Search on the Answer.

        Intuition:
        If Koko eats at speed k:
        - For a pile with `p` bananas, the hours required is ceil(p / k) = (p + k - 1) // k.
        - Total hours required is sum((p + k - 1) // k for p in piles).
        
        Monotonic Property:
        - As eating speed k increases, total hours required monotonically decreases (or stays the same).
        - If speed k allows Koko to finish within h hours, any speed > k also works.
        - If speed k is too slow, any speed < k is also too slow.
        - This monotonic predicate allows us to binary search for the minimum valid speed k.

        Search Space:
        - Minimum possible speed: left = 1 (must eat at least 1 banana per hour).
        - Maximum possible speed: right = max(piles) (since h >= len(piles), eating at speed
          max(piles) takes exactly len(piles) <= h hours; higher speeds do not save any extra hours).

        Algorithm:
        1. Initialize `left = 1`, `right = max(piles)`, `ans = right`.
        2. While `left <= right`:
           - mid = left + (right - left) // 2
           - Compute total hours needed at speed `mid`:
             total_hours = sum((p + mid - 1) // mid for p in piles)
           - If total_hours <= h:
             Speed `mid` is feasible. Record `ans = mid` and search left half (`right = mid - 1`)
             to test if a slower speed is possible.
           - Else:
             Speed `mid` is too slow. Search right half (`left = mid + 1`).
        3. Return `ans`.

        Complexity:
        - Time Complexity: O(N * log(max(piles))) where N = len(piles).
          Since max(piles) <= 10^9, log2(max(piles)) <= 30 iterations.
        - Space Complexity: O(1) auxiliary space.
        """
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = left + (right - left) // 2

            # Compute hours required to eat all piles at speed mid
            hours_needed = 0
            for p in piles:
                hours_needed += (p + mid - 1) // mid

            if hours_needed <= h:
                ans = mid
                right = mid - 1  # Try slower speed
            else:
                left = mid + 1   # Must eat faster

        return ans


# --- Unit Tests ---
def test_min_eating_speed():
    solver = Solution()

    # Test Case 1: LeetCode Example 1
    # piles = [3, 6, 7, 11], h = 8
    # k = 4: ceil(3/4)=1, ceil(6/4)=2, ceil(7/4)=2, ceil(11/4)=3 -> 1+2+2+3 = 8 <= 8
    assert solver.minEatingSpeed([3, 6, 7, 11], 8) == 4, "TC1 failed"

    # Test Case 2: LeetCode Example 2
    # piles = [30, 11, 23, 4, 20], h = 5
    # Since h == len(piles), Koko must finish each pile in 1 hour -> k = max(piles) = 30
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30, "TC2 failed"

    # Test Case 3: LeetCode Example 3
    # piles = [30, 11, 23, 4, 20], h = 6
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23, "TC3 failed"

    # Test Case 4: Single pile
    # piles = [10], h = 2 -> k = 5 (2 hours)
    assert solver.minEatingSpeed([10], 2) == 5, "TC4 failed"

    # Test Case 5: Single pile with h == pile size
    # piles = [10], h = 10 -> k = 1
    assert solver.minEatingSpeed([10], 10) == 1, "TC5 failed"

    # Test Case 6: h much larger than sum of piles -> k = 1
    assert solver.minEatingSpeed([1, 1, 1, 1], 100) == 1, "TC6 failed"

    # Test Case 7: Uniform piles
    # piles = [5, 5, 5, 5], h = 4 -> k = 5
    assert solver.minEatingSpeed([5, 5, 5, 5], 4) == 5, "TC7 failed"

    # Test Case 8: Uniform piles with h double the count -> k = 3
    # ceil(5/3) = 2 hours per pile -> 4 * 2 = 8 hours
    assert solver.minEatingSpeed([5, 5, 5, 5], 8) == 3, "TC8 failed"

    # Test Case 9: Large values
    # piles = [1000000000], h = 2 -> k = 500000000
    assert solver.minEatingSpeed([1000000000], 2) == 500000000, "TC9 failed"

    # Test Case 10: Non-trivial division with exact hours
    # piles = [312884470], h = 312884469 -> k = 2
    assert solver.minEatingSpeed([312884470], 968709470) == 1, "TC10 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_min_eating_speed()
