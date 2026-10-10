# Day 22: Minimum Window Substring

- **Problem Link:** [LeetCode #76 - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- **Difficulty:** 🔴 Hard
- **Topic:** Sliding Window
- **Date Solved:** 2026-10-10

---

## 📝 Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

### Example 1:
```text
Input:  s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```text
Input:  s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3:
```text
Input:  s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

### Constraints:
- `m == s.length`, `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

---

## 💡 Algorithmic Approaches

### 1. Brute Force
- Check all possible substrings of `s` and verify if each contains all required character frequencies of `t`.
- **Time Complexity:** $O(m^2 \cdot n)$ — Will encounter Time Limit Exceeded for $m, n = 10^5$.
- **Space Complexity:** $O(n)$.

### 2. Two-Phase Variable Sliding Window (Optimal) 🚀
- Use two pointers `left` and `right` forming window `s[left:right+1]`.
- Track:
  - `target_counts`: Frequencies of characters required by `t`.
  - `required`: Number of distinct characters in `t` that must meet target frequency.
  - `formed`: Number of distinct characters currently satisfying target frequency in the window.
- **Phase 1: Expansion (`right` moves forward)**
  - Expand the window by adding `s[right]`.
  - If `window_counts[s[right]] == target_counts[s[right]]`, increment `formed`.
- **Phase 2: Contraction (`left` moves forward)**
  - While `formed == required` (window is valid):
    - Update the best window if current length `right - left + 1` is smaller than best seen.
    - Remove `s[left]` from the window.
    - If `window_counts[s[left]] < target_counts[s[left]]`, decrement `formed`.
    - Advance `left += 1`.
- **Time Complexity:** $O(m + n)$ — Each character is visited at most twice (once by right, once by left).
- **Space Complexity:** $O(m + n)$ (bounded by alphabet size, $O(52) = O(1)$ for English letters).

---

## 💻 Python Implementation

```python
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_counts = Counter(t)
        required = len(target_counts)

        window_counts = defaultdict(int)
        formed = 0

        best_window = (float("inf"), None, None)
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1

            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            while formed == required and left <= right:
                window_len = right - left + 1
                if window_len < best_window[0]:
                    best_window = (window_len, left, right)

                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1

                left += 1

        if best_window[0] == float("inf"):
            return ""

        return s[best_window[1]:best_window[2] + 1]
```

---

## 🔑 Sliding Window Dynamic Expansion & Contraction

```
s = "A D O B E C O D E B A N C", t = "ABC"

Expand until valid:
[A D O B E C]           Valid! (len 6) -> Contract from left:
  [D O B E C]           Invalid ('A' lost)

Expand right until valid again:
  [D O B E C O D E B A] Valid! (len 9) -> Contract:
    [O B E C O D E B A]
      [B E C O D E B A]
        [C O D E B A]   Valid! (len 6)

Expand right again:
        [C O D E B A N C] Valid! -> Contract:
                [B A N C] Valid! (len 4, Best!)
                  [A N C] Invalid ('B' lost)

Minimum Window: "BANC"
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard case with multiple contractions (`"ADOBECODEBANC"`, `"ABC"` → `"BANC"`)
2. Exact single character match (`"a"`, `"a"` → `"a"`)
3. Impossible match (`"a"`, `"aa"` → `""`)
4. Target longer than source (`"ab"`, `"abc"` → `""`)
5. Duplicate target requirements (`"AABBCC"`, `"AAB"` → `"AAB"`)
6. Exact whole string match (`"HELLO"`, `"HELLO"` → `"HELLO"`)
7. Window located at string start (`"ABXYZCD"`, `"AB"` → `"AB"`)
8. Window located at string end (`"XYZABCD"`, `"CD"` → `"CD"`)
9. Tight cluster occurring after dispersed noise (`"AAABBBCCOAABBCC"`, `"ABC"` → `"ABBC"`)
10. Case-sensitive matching (`"aAbBcC"`, `"AB"` → `"AbB"`)
