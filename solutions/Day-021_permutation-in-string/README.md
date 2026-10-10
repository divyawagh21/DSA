# Day 21: Permutation in String

- **Problem Link:** [LeetCode #567 - Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- **Difficulty:** 🟡 Medium
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-10

---

## 📝 Problem Statement

Given two strings `s1` and `s2`, return `true` if `s2` contains a **permutation** of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the **substring** of `s2`.

### Example 1:
```text
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2:
```text
Input:  s1 = "ab", s2 = "eidboaoo"
Output: false
```

### Constraints:
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

---

## 💡 Algorithmic Approaches

### 1. Brute Force (Generate All Permutations)
- Generate all $n!$ permutations of `s1` and search for each in `s2`.
- **Time Complexity:** $O(n! \cdot m)$ — Factorial blowup, completely infeasible.
- **Space Complexity:** $O(n!)$.

### 2. Fixed-Size Sliding Window with Array Comparison
- Permutations share the exact same character frequencies.
- Any valid permutation of `s1` within `s2` must be a contiguous window of length $k = |s1|$.
- Slide a window of length $k$ across `s2`, checking if `s1_counts == window_counts`.
- **Time Complexity:** $O(26 \cdot |s2|) = O(|s2|)$.
- **Space Complexity:** $O(26) = O(1)$.

### 3. Optimized Sliding Window with O(1) Match Counter (Optimal) 🚀
- Instead of comparing all 26 elements at each step, maintain a `matches` scalar (ranging from 0 to 26).
- A character has a "match" if its frequency in the window equals its frequency in `s1`.
- As the window slides:
  - Add the new incoming character on the right: update `matches` in $O(1)$.
  - Remove the outgoing character on the left: update `matches` in $O(1)$.
- Return `true` immediately when `matches == 26`.
- **Time Complexity:** $O(|s2|)$ strict linear time with minimal constant factor.
- **Space Complexity:** $O(26) = O(1)$ space.

---

## 💻 Python Implementation

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1

        matches = sum(1 for i in range(26) if s1_counts[i] == s2_counts[i])

        for r in range(n1, n2):
            if matches == 26:
                return True

            idx_in = ord(s2[r]) - ord("a")
            s2_counts[idx_in] += 1
            if s2_counts[idx_in] == s1_counts[idx_in]:
                matches += 1
            elif s2_counts[idx_in] == s1_counts[idx_in] + 1:
                matches -= 1

            l = r - n1
            idx_out = ord(s2[l]) - ord("a")
            s2_counts[idx_out] -= 1
            if s2_counts[idx_out] == s1_counts[idx_out]:
                matches += 1
            elif s2_counts[idx_out] == s1_counts[idx_out] - 1:
                matches -= 1

        return matches == 26
```

---

## 🔑 Fixed-Size Sliding Window Visualization

```
s1 = "ab" (len = 2, counts = {a:1, b:1})
s2 = "e i d b a o o o"

Window [e i]: {e:1, i:1}         matches = 24  ≠ 26
Window [i d]: {i:1, d:1}         matches = 24  ≠ 26
Window [d b]: {d:1, b:1}         matches = 25  ≠ 26
Window [b a]: {a:1, b:1}         matches = 26  == 26  -> FOUND! True
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard permutation inside string (`"ab"`, `"eidbaooo"` → `True`)
2. Dispersed characters without contiguous substring (`"ab"`, `"eidboaoo"` → `False`)
3. Length constraint: `s1` longer than `s2` (`"abcde"`, `"ab"` → `False`)
4. Exact identical strings (`"abc"`, `"abc"` → `True`)
5. Permutation located at the tail of `s2` (`"adc"`, `"dcda"` → `True`)
6. Single character matching (`"a"`, `"a"` → `True`)
7. Single character mismatch (`"a"`, `"b"` → `False`)
8. Frequency mismatch with duplicated characters (`"hello"`, `"ooolleoooleh"` → `False`)
9. Repeated character match (`"aab"`, `"baab"` → `True`)
10. Match located in middle of complex sequence (`"xyz"`, `"afkzxye"` → `True`)
