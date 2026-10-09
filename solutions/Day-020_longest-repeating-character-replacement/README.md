# Day 20: Longest Repeating Character Replacement

- **Problem Link:** [LeetCode #424 - Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- **Difficulty:** 🟡 Medium
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-09

---

## 📝 Problem Statement

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the **longest substring containing the same letter** you can get after performing the above operations.

### Example 1:
```text
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2:
```text
Input:  s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has length 4. There may exists other ways to achieve this answer too.
```

### Constraints:
- `1 <= s.length <= 10^5`
- `0 <= k <= s.length`
- `s` consists of only uppercase English letters.

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Check every substring `(i, j)`.
- Find the most frequent character in that window.
- If `(window_len - max_freq) <= k`, it is valid.
- **Time Complexity:** $O(N^2 \cdot 26)$ — Unacceptable for $N = 10^5$.
- **Space Complexity:** $O(26) = O(1)$.

### 2. Sliding Window with Running Max Frequency (Optimal) 🚀
- For any window `[left, right]`:
  $$\text{replacements\_needed} = (\text{right} - \text{left} + 1) - \text{max\_frequency}$$
- If $\text{replacements\_needed} \le k$, the window can be converted into a uniform character block!
- If $\text{replacements\_needed} > k$, shrink the window from `left`.
- **Crucial Optimization:** We never need to decrease `max_frequency` when shrinking `left`. A smaller `max_frequency` would only yield a smaller window, which cannot beat the best window length already discovered!
- **Time Complexity:** $O(N)$ — Left and right pointers only move forward.
- **Space Complexity:** $O(26) = O(1)$ auxiliary memory.

---

## 💻 Python Implementation

```python
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            if counts[s[right]] > max_freq:
                max_freq = counts[s[right]]

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            window_len = right - left + 1
            if window_len > max_len:
                max_len = window_len

        return max_len
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Two-replacement standard case (`"ABAB"`, k=2 → `4`)
2. Alternating pattern with single replacement (`"AABABBA"`, k=1 → `4`)
3. Zero replacements allowed (`"ABCDE"`, k=0 → `1`)
4. Zero replacements with existing streaks (`"ABBBBA"`, k=0 → `4`)
5. Replacement budget exceeding string length (`"ABC"`, k=10 → `3`)
6. Single character boundary case (`"Z"`, k=1 → `1`)
7. Monotonous input requiring zero edits (`"AAAA"`, k=2 → `4`)
8. Boundary substitutions on ends (`"BAAAB"`, k=2 → `5`)
9. Sparse noisy string (`"KRSCDCSONAJNHLBMAQEZTXCOABG"`, k=3 → `5`)
10. Alternating pattern with $k=0$ (`"ABAA"`, k=0 → `2`)
