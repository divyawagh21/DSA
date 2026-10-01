# Day 12: Longest Consecutive Sequence

- **Problem Link:** [LeetCode #128 - Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- **Difficulty:** 🟡 Medium
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-10-01

---

## 📝 Problem Statement

Given an unsorted array of integers `nums`, return the length of the **longest consecutive elements sequence**.

> **Requirement:** Must run in $O(N)$ time.

### Example 1:
```text
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: Longest sequence is [1, 2, 3, 4].
```

### Example 2:
```text
Input:  nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation: Longest sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8].
```

### Constraints:
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## 💡 Algorithmic Approaches

### 1. Sort and Scan
- Sort `nums`, then scan for runs of consecutive integers.
- **Time Complexity:** $O(N \log N)$ — violates the follow-up constraint.
- **Space Complexity:** $O(1)$ extra.

### 2. Hash Set + Sequence-Start Optimisation (Optimal) 🚀

**Key Insight:** A number `n` is the **start** of a consecutive sequence if and only if `n - 1` is **not** in the set. By skipping all non-starts, we guarantee each sequence is explored exactly once.

**Algorithm:**
1. Load all numbers into a `set` → $O(N)$ build, $O(1)$ lookups.
2. For each `n` in the set:
   - If `n - 1 ∈ set`: skip (middle of an existing sequence).
   - Else: count upward `n+1`, `n+2`... and track the run length.
3. Return `max(best, length)`.

**Why O(N)?**
Each element is visited in the outer loop once AND in the inner while loop at most once (as part of exactly one sequence). Total work ≤ 2N.

- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ — the hash set

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        best = 0

        for n in num_set:
            if n - 1 not in num_set:   # sequence start
                current, length = n, 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                best = max(best, length)

        return best
```

---

## 🔑 Key Insight Visualised

```
nums = [100, 4, 200, 1, 3, 2]
set  = {1, 2, 3, 4, 100, 200}

n=1   → 0 not in set  → START → count 1,2,3,4 → length=4 ✓
n=2   → 1 in set      → SKIP
n=3   → 2 in set      → SKIP
n=4   → 3 in set      → SKIP
n=100 → 99 not in set → START → count 100 → length=1
n=200 → 199 not in set→ START → count 200 → length=1

Answer: 4
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests covering:
1. LeetCode Example 1 — scattered numbers, sequence of 4
2. LeetCode Example 2 — longer sequence with duplicates and gaps
3. Empty array → 0
4. Single element → 1
5. All identical elements (duplicates) → 1
6. Already sorted consecutive → full length
7. Negative numbers in sequence
8. Two separate equal-length sequences
9. Large gap with sequences of different lengths
10. Array with duplicates
