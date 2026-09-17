"""
LeetCode #1: Two Sum
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-17

Problem:
Given an array of integers `nums` and an integer `target`, return indices
of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.
You can return the answer in any order.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in nums that add up to target using a One-Pass Hash Map.
        
        Intuition:
        For every element `num` at index `i`, its required complement is `target - num`.
        Instead of searching the rest of the array with a nested loop (O(N^2)),
        we maintain a hash map of {seen_number: index}.
        If the complement is already in the map, we have found our two indices.
        Otherwise, we store the current number with its index and continue.
        
        Complexity:
        - Time Complexity: O(N) since dictionary lookup and insertion take O(1) on average.
        - Space Complexity: O(N) to store up to N elements in the hash map.
        """
        seen = {}  # maps number -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            
        return []


# --- Unit Tests ---
def test_two_sum():
    solver = Solution()
    
    # Test Case 1: Standard case
    res1 = solver.twoSum([2, 7, 11, 15], 9)
    assert sorted(res1) == [0, 1], f"Expected [0, 1], got {res1}"
    
    # Test Case 2: Adjacent pair
    res2 = solver.twoSum([3, 2, 4], 6)
    assert sorted(res2) == [1, 2], f"Expected [1, 2], got {res2}"
    
    # Test Case 3: Duplicate numbers
    res3 = solver.twoSum([3, 3], 6)
    assert sorted(res3) == [0, 1], f"Expected [0, 1], got {res3}"
    
    # Test Case 4: Negative numbers
    res4 = solver.twoSum([-1, -2, -3, -4, -5], -8)
    assert sorted(res4) == [2, 4], f"Expected [2, 4], got {res4}"
    
    # Test Case 5: Target with zero
    res5 = solver.twoSum([0, 4, 3, 0], 0)
    assert sorted(res5) == [0, 3], f"Expected [0, 3], got {res5}"
    
    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_two_sum()