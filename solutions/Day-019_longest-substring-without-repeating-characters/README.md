# Day 19: Longest Substring Without Repeating Characters

- **Problem Link:** [LeetCode #3 - Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **Difficulty:** 🟡 Medium
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-09

---

## 📝 Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Example 1:
```text
Input:  s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```text
Input:  s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```text
Input:  s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Check all possible substrings `(i, j)` and test each for uniqueness using a set.
- **Time Complexity:** $O(N^3)$ or $O(N^2)$ — Infeasible for $N = 50,000$.
- **Space Complexity:** $O(min(N, M))$.

### 2. Standard Sliding Window with Set
- Use two pointers `left` and `right`.
- Expand `right`. If `s[right]` is already in `seen_set`, incrementally shrink `left` while discarding `s[left]` until `s[right]` is removed.
- **Time Complexity:** $O(2N) = O(N)$ — In the worst case, every character is visited twice (once by right, once by left).
- **Space Complexity:** $O(min(N, M))$.

### 3. Optimized Sliding Window with Last-Seen Map (Optimal) 🚀
- Instead of shrinking `left` one step at a time, store the **most recent index** of each character in a hash map `last_seen`.
- When encountering a character whose previous index $\ge left$, jump `left` directly to `last_seen[char] + 1` in $O(1)$.
- Window length at any step is `right - left + 1`.
- **Time Complexity:** $O(N)$ — Strict single pass over the string.
- **Space Complexity:** $O(min(N, M))$ where $M$ is the size of the character set (at most 128 for ASCII or 256 for extended).

---

## 💻 Python Implementation

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            last_seen[char] = right
            window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len

        return max_len
```

---

## 🔑 Sliding Window Dynamic Contraction

```
s = "a b c a b c b b"
     ▲   ▲
   left right=3 ('a' duplicate seen at idx 0)
   Jump left to 0 + 1 = 1:
     [b c a] -> length = 3
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard repeating cycle (`"abcabcbb"` → `3`)
2. Monotonous repetition (`"bbbbb"` → `1`)
3. Repeated prefix with unique interior (`"pwwkew"` → `3`)
4. Empty string boundary case (`""` → `0`)
5. Whitespace character (`" "` → `1`)
6. Strictly distinct string (`"abcdef"` → `6`)
7. Mirrored duplicate pattern (`"abba"` → `2`)
8. Symbols, digits, and special characters (`"a!b@c#1$2%3^"` → `12`)
9. Non-trivial skip with trailing repetition (`"tmmzuxt"` → `5`)
10. Interior jump test case (`"dvdf"` → `3`)
