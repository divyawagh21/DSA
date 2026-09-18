"""
LeetCode #217: Contains Duplicate
Difficulty: Easy
Topic: Arrays & Hashing
Date Solved: 2026-09-18

Problem:
Given an integer array `nums`, return true if any value appears at least twice
in the array, and return false if every element is distinct.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if the array contains any duplicates using an early-exit Hash Set.
        
        Intuition:
        A hash set provides O(1) average time complexity for both membership checks
        and insertions. As we iterate through the array, we check if the current element
        has already been seen:
        - If it is already present in our set, a duplicate exists, so we return True immediately.
        - If not, we add it to the set and continue.
        If we finish iterating through the entire list without finding any duplicate,
        we return False.
        
        Complexity:
        - Time Complexity: O(N) in the worst case (where all elements are distinct),
          and O(K) on average when a duplicate is found early (where K is the index of the duplicate).
        - Space Complexity: O(N) to store up to N unique elements in the hash set.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# --- Unit Tests ---
def test_contains_duplicate():
    solver = Solution()
    
    # Test Case 1: Simple array with duplicate at boundaries
    nums1 = [1, 2, 3, 1]
    assert solver.containsDuplicate(nums1) is True, f"Failed on {nums1}"
    
    # Test Case 2: All distinct elements
    nums2 = [1, 2, 3, 4]
    assert solver.containsDuplicate(nums2) is False, f"Failed on {nums2}"
    
    # Test Case 3: Multiple duplicates of several numbers
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solver.containsDuplicate(nums3) is True, f"Failed on {nums3}"
    
    # Test Case 4: Single element array (minimum constraint boundary)
    nums4 = [42]
    assert solver.containsDuplicate(nums4) is False, f"Failed on {nums4}"
    
    # Test Case 5: Two identical elements
    nums5 = [7, 7]
    assert solver.containsDuplicate(nums5) is True, f"Failed on {nums5}"
    
    # Test Case 6: Negative numbers and zeros
    nums6 = [-1, 0, 1, -1]
    assert solver.containsDuplicate(nums6) is True, f"Failed on {nums6}"
    
    # Test Case 7: Large numbers
    nums7 = [1000000000, -1000000000, 1000000000]
    assert solver.containsDuplicate(nums7) is True, f"Failed on {nums7}"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_contains_duplicate()
