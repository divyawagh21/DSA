# Day 09: Top K Frequent Elements

- **Problem Link:** [LeetCode #347 - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- **Difficulty:** 🟡 Medium
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-26

---

## 📝 Problem Statement

Given an integer array `nums` and an integer `k`, return the **k most frequent elements**. You may return the answer in any order.

> **Follow-up:** Your algorithm's time complexity must be better than $O(N \log N)$.

### Example 1:
```text
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1, 2]
```

### Example 2:
```text
Input:  nums = [1], k = 1
Output: [1]
```

### Constraints:
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, number of unique elements in nums]`
- The answer is **guaranteed to be unique**.

---

## 💡 Algorithmic Approaches

### 1. Sort by Frequency
- Count frequencies with a hash map, then sort items by frequency descending.
- Return the first `k` keys.
- **Time Complexity:** $O(N \log N)$ — violates the follow-up constraint.
- **Space Complexity:** $O(N)$

### 2. Min-Heap of Size k
- Build frequency map: $O(N)$.
- Use `heapq.nlargest(k, freq, key=freq.get)`: $O(N \log k)$.
- **Time Complexity:** $O(N \log k)$ — satisfies the follow-up when $k \ll N$.
- **Space Complexity:** $O(N)$

### 3. Bucket Sort (Optimal) 🚀
- **Key Insight:** The maximum possible frequency is $N$ (all elements identical). So we can create an array of $N+1$ frequency buckets where `bucket[f]` holds all numbers appearing exactly `f` times.
- **Steps:**
  1. Count frequencies: $O(N)$.
  2. Place each number into `buckets[freq]`: $O(N)$.
  3. Scan buckets from index $N$ down to $1$, collecting until we have $k$ results: $O(N)$.
- **Time Complexity:** $O(N)$ — strictly beats $O(N \log N)$.
- **Space Complexity:** $O(N)$ — frequency map + bucket array.

---

## 💻 Python Implementation

```python
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for f in range(len(buckets) - 1, 0, -1):
            for num in buckets[f]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
```

---

## 🧪 Verification & Test Cases

The solution includes 8 automated unit tests (order-independent comparison):
1. LeetCode Example 1 — `[1,1,1,2,2,3]`, k=2 → `[1,2]`
2. LeetCode Example 2 — `[1]`, k=1 → `[1]`
3. k equals total unique elements → all elements returned
4. All identical elements, k=1
5. Negative numbers → most frequent is negative
6. Tied frequencies — either valid answer accepted
7. Larger input with clear top-2 winners
8. Single clear winner with k=1
