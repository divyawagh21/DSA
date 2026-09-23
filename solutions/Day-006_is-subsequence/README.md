# Day 06: Is Subsequence

- **Problem Link:** [LeetCode #392 - Is Subsequence](https://leetcode.com/problems/is-subsequence/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-23

---

## 📝 Problem Statement

Given two strings `s` and `t`, return `true` if `s` is a **subsequence** of `t`, or `false` otherwise.

A **subsequence** is a string formed by deleting some (possibly zero) characters from the original string without changing the relative order of the remaining characters.

### Example 1:
```text
Input:  s = "ace", t = "abcde"
Output: true
Explanation: 'a', 'c', 'e' appear in that order within "abcde".
```

### Example 2:
```text
Input:  s = "aec", t = "abcde"
Output: false
Explanation: 'e' comes before 'c' in "abcde", so the order is violated.
```

### Constraints:
- `0 <= s.length <= 100`
- `0 <= t.length <= 10^4`
- `s` and `t` consist only of lowercase English letters.

### Follow-up:
If there are many incoming `s` queries for the same `t` (e.g., `s1`, `s2`, ..., `sk` against a fixed `t`), how would you optimize your solution?

---

## 💡 Algorithmic Approaches

### 1. Two-Pointer (Optimal for Single Query) 🚀
- Maintain pointer `sp` into `s` and scan through `t` character by character.
- Whenever `t[tp] == s[sp]`, advance `sp` (a character is matched).
- If `sp` reaches `len(s)` at any point, all characters matched — return `True`.
- If `t` is fully exhausted before `sp == len(s)` — return `False`.
- **Time Complexity:** $O(N)$ where $N = |t|$ — single scan of `t`.
- **Space Complexity:** $O(1)$ — only two integer pointers.

### 2. Binary Search Pre-processing (Optimal for Many Queries)
- Pre-process `t` into a dictionary `{char → sorted list of indices}`.
- For each query `s`, binary search (`bisect_left`) to find the next valid position in `t` for each character of `s`.
- **Pre-processing:** $O(|t|)$ time and space.
- **Per Query:** $O(|s| \log |t|)$ — binary search for each character in `s`.

---

## 💻 Python Implementation

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0  # pointer into s

        for char in t:
            if sp == len(s):
                break
            if char == s[sp]:
                sp += 1

        return sp == len(s)
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests covering:
1. LeetCode Example 1 — `"ace"` in `"abcde"` → `True`
2. LeetCode Example 2 — `"aec"` in `"abcde"` → `False`
3. Empty `s` — always `True` for any `t`
4. Both empty — `True`; non-empty `s` vs empty `t` — `False`
5. `s == t` exactly — `True`
6. `len(s) > len(t)` — impossible, `False`
7. Single char present in `t`
8. Single char absent from `t`
9. Characters present but out of order (`"axc"` in `"ahbgdc"`)
10. Duplicate characters in `t` (`"aa"` in `"aabaa"`)
