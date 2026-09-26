"""
LeetCode #347: Top K Frequent Elements
Difficulty: Medium
Topic: Arrays & Hashing
Date Solved: 2026-09-26

Problem:
Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order.

Follow-up constraint: Your algorithm's time complexity must be better than
O(N log N), where N is the array's size.
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Return the k most frequent elements using Bucket Sort on frequencies.

        Intuition:
        The naive approach (sort by frequency) takes O(N log N). We can do
        better using a clever observation: the maximum possible frequency for
        any element is N (when all elements are the same). So we can create
        N+1 "frequency buckets" where bucket[f] holds all numbers that appear
        exactly f times.

        Algorithm:
        1. Count frequencies of each number using a hash map → O(N).
        2. Create a bucket array of size N+1 (indices 0..N).
           Place each number into bucket[frequency].
        3. Traverse buckets from highest frequency (N) down to 1.
           Collect numbers until we have k results → O(N).

        This achieves O(N) overall, satisfying the follow-up constraint.

        Alternative approach — Min-Heap of size k:
        - Build frequency map: O(N).
        - Use heapq.nlargest(k, freq.items(), key=lambda x: x[1]): O(N log k).
        - This is O(N log k) which is better than O(N log N) when k << N, but
          bucket sort is strictly O(N).

        Complexity (Bucket Sort approach):
        - Time Complexity: O(N) — frequency count O(N) + bucket build O(N) +
          bucket scan O(N).
        - Space Complexity: O(N) — frequency map + bucket array both O(N).
        """
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Build frequency buckets (index = frequency count)
        # Index range: 0 to len(nums) inclusive
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Collect top-k from highest frequency bucket downward
        result = []
        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result

        return result  # Should always return inside the loop for valid input


# --- Unit Tests ---
def test_top_k_frequent():
    solver = Solution()

    # Helper: compare results as sets (order doesn't matter)
    def same(result, expected):
        return sorted(result) == sorted(expected)

    # Test Case 1: LeetCode Example 1
    assert same(solver.topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2]), "TC1 failed"

    # Test Case 2: LeetCode Example 2 — k=1, only one element
    assert same(solver.topKFrequent([1], 1), [1]), "TC2 failed"

    # Test Case 3: k equals total unique elements
    assert same(solver.topKFrequent([1, 2, 3], 3), [1, 2, 3]), "TC3 failed"

    # Test Case 4: All elements identical
    assert same(solver.topKFrequent([5, 5, 5, 5], 1), [5]), "TC4 failed"

    # Test Case 5: Negative numbers
    assert same(solver.topKFrequent([-1, -1, 2, 2, 2], 1), [2]), "TC5 failed"

    # Test Case 6: Two elements tied for top but k=1
    # Both 1 and 2 appear twice; either could be in the result
    result6 = solver.topKFrequent([1, 1, 2, 2], 1)
    assert result6[0] in [1, 2], "TC6 failed"

    # Test Case 7: Larger input
    nums7 = [4, 4, 4, 6, 6, 7, 7, 7, 7, 8]
    assert same(solver.topKFrequent(nums7, 2), [7, 4]), "TC7 failed"

    # Test Case 8: k equals 1 with clear winner
    assert same(solver.topKFrequent([3, 0, 1, 0], 1), [0]), "TC8 failed"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_top_k_frequent()
