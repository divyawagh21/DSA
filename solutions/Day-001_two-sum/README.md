# Day 01: Two Sum

- **Problem Link:** [LeetCode #1 - Two Sum](https://leetcode.com/problems/two-sum/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-17

---

## 📝 Problem Statement

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:
```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:
```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- **Only one valid answer exists.**

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Iterate through each element with a nested loop `for i in range(n)` and `for j in range(i + 1, n)`.
- Check if `nums[i] + nums[j] == target`.
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(1)$

### 2. One-Pass Hash Map (Optimal) 🚀
- As we traverse the array, we compute the required `complement = target - nums[i]`.
- We check if `complement` is already stored in our hash map:
  - If **yes**, return `[seen[complement], i]`.
  - If **no**, store `seen[nums[i]] = i`.
- This reduces the lookup time from $O(N)$ to average $O(1)$.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$

---

## 💻 Python Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
```

---

## 🧪 Verification & Test Cases

The solution includes a test suite covering:
1. Standard increasing array (`[2, 7, 11, 15]`, target: `9`)
2. Target formed by non-consecutive indices (`[3, 2, 4]`, target: `6`)
3. Identical elements (`[3, 3]`, target: `6`)
4. Negative numbers (`[-1, -2, -3, -4, -5]`, target: `-8`)
5. Arrays containing zeros (`[0, 4, 3, 0]`, target: `0`)