"""
LeetCode #239: Sliding Window Maximum
Difficulty: Hard
Topic: Sliding Window
Date Solved: 2026-10-11

Problem:
You are given an array of integers `nums`, there is a sliding window of size `k`
which is moving from the very left of the array to the very right. You can only
see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Find the maximum in each sliding window of size k using a Monotonic Decreasing Deque.

        Intuition:
        A brute-force approach finds the max of each size-k window in O(k), giving O(N * k)
        total time, which times out for N = 10^5 and k = 10^5.
        A max-heap approach takes O(N log N) or O(N log k).

        We can achieve strict O(N) linear time using a Monotonic Decreasing Deque:
        - Store INDICES in a double-ended queue (`deque`).
        - The values corresponding to the stored indices are maintained in strictly
          decreasing order: `nums[deque[0]] > nums[deque[1]] > ... > nums[deque[-1]]`.
        - The front of the deque (`deque[0]`) will always be the index of the MAXIMUM
          element in the current window.

        Algorithm:
        For each index `i` from 0 to len(nums) - 1:
        1. Remove indices from the FRONT if they fall outside the current window:
           `deque[0] <= i - k`.
        2. Remove indices from the BACK while the new element `nums[i]` is greater than
           or equal to `nums[deque[-1]]`. Any element smaller than `nums[i]` can NEVER
           be the maximum in this or any future window because `nums[i]` is both larger
           and will remain in future windows longer!
        3. Append the current index `i` to the back.
        4. Once the first window of size `k` is reached (i.e. `i >= k - 1`), record
           `nums[deque[0]]` into our result list.

        Complexity:
        - Time Complexity: O(N) — Each element is added to the deque once and removed
          at most once across the entire iteration.
        - Space Complexity: O(k) — Auxiliary space for the deque, which holds at most k indices.
        """
        if not nums or k <= 0:
            return []
        if k == 1:
            return nums

        dq = deque()
        result = []

        for i, val in enumerate(nums):
            # 1. Pop elements outside current window boundary
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Maintain monotonic decreasing order (pop smaller elements from back)
            while dq and nums[dq[-1]] <= val:
                dq.pop()

            # 3. Add current element index
            dq.append(i)

            # 4. Record maximum once window size k is reached
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# --- Unit Tests ---
def test_max_sliding_window():
    solver = Solution()

    # Test Case 1: Standard case from LeetCode
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    expected1 = [3, 3, 5, 5, 6, 7]
    assert solver.maxSlidingWindow(nums1, k1) == expected1, f"TC1 failed on {nums1}"

    # Test Case 2: Single element array with k=1
    nums2 = [1]
    k2 = 1
    expected2 = [1]
    assert solver.maxSlidingWindow(nums2, k2) == expected2, f"TC2 failed on {nums2}"

    # Test Case 3: Strictly decreasing array
    nums3 = [9, 8, 7, 6, 5, 4]
    k3 = 3
    expected3 = [9, 8, 7, 6]
    assert solver.maxSlidingWindow(nums3, k3) == expected3, f"TC3 failed on {nums3}"

    # Test Case 4: Strictly increasing array
    nums4 = [1, 2, 3, 4, 5, 6]
    k4 = 3
    expected4 = [3, 4, 5, 6]
    assert solver.maxSlidingWindow(nums4, k4) == expected4, f"TC4 failed on {nums4}"

    # Test Case 5: Window size k equals array length
    nums5 = [4, 2, 7, 1, 9]
    k5 = 5
    expected5 = [9]
    assert solver.maxSlidingWindow(nums5, k5) == expected5, f"TC5 failed on {nums5}"

    # Test Case 6: Window size k=1 (each element is its own max)
    nums6 = [2, 1, 5, 3]
    k6 = 1
    expected6 = [2, 1, 5, 3]
    assert solver.maxSlidingWindow(nums6, k6) == expected6, f"TC6 failed on {nums6}"

    # Test Case 7: All identical elements
    nums7 = [5, 5, 5, 5, 5]
    k7 = 2
    expected7 = [5, 5, 5, 5]
    assert solver.maxSlidingWindow(nums7, k7) == expected7, f"TC7 failed on {nums7}"

    # Test Case 8: Negative numbers
    nums8 = [-7, -8, -7, 5, 7, 1, 6, 0]
    k8 = 4
    expected8 = [5, 7, 7, 7, 7]
    assert solver.maxSlidingWindow(nums8, k8) == expected8, f"TC8 failed on {nums8}"

    # Test Case 9: Window with alternating peaks and troughs
    nums9 = [1, 3, 1, 2, 0, 5]
    k9 = 3
    expected9 = [3, 3, 2, 5]
    assert solver.maxSlidingWindow(nums9, k9) == expected9, f"TC9 failed on {nums9}"

    # Test Case 10: Two-element window with duplicate values
    nums10 = [1, -1]
    k10 = 1
    expected10 = [1, -1]
    assert solver.maxSlidingWindow(nums10, k10) == expected10, f"TC10 failed on {nums10}"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_max_sliding_window()
