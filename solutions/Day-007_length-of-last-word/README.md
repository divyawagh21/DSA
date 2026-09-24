# Day 07: Length of Last Word

- **Problem Link:** [LeetCode #58 - Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-24

---

## 📝 Problem Statement

Given a string `s` consisting of words and spaces, return the length of the **last** word in the string.

A **word** is a maximal substring consisting of non-space characters only.

### Example 1:
```text
Input:  s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

### Example 2:
```text
Input:  s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

### Example 3:
```text
Input:  s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

---

## 💡 Algorithmic Approaches

### 1. Reverse Traversal / Backward Pointer (Optimal $O(1)$ Space) 🚀
- Place pointer `i` at the final index: `len(s) - 1`.
- **Phase 1 (Trim):** Move backward past any trailing whitespace characters (`s[i] == ' '`).
- **Phase 2 (Count):** Count non-space characters until encountering a space or the start of the string (`i < 0`).
- **Time Complexity:** $O(N)$ worst case (e.g., single word preceded by spaces), practically $O(K)$ where $K$ is the distance from the end of the string to the start of the last word.
- **Space Complexity:** $O(1)$ auxiliary memory since we avoid allocating sub-strings or arrays of tokens.

### 2. Built-in Strip & Split (Pythonic)
- Strip trailing spaces with `.rstrip()` and extract the last token with `.split(" ")[-1]`.
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$ to hold the split tokens in memory.

---

## 💻 Python Implementation

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        # Step 1: Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Step 2: Count characters of the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
```

---

## 🧪 Verification & Test Cases

The solution includes 8 automated unit tests covering:
1. Standard two-word sentence (`"Hello World"` → `5`)
2. Leading, multiple intermediate, and trailing spaces (`"   fly me   to   the moon  "` → `4`)
3. Multi-word phrase (`"luffy is still joyboy"` → `6`)
4. Single letter and single word without spaces (`"a"` → `1`, `"algorithm"` → `9`)
5. Single word surrounded by spaces (`"   code   "` → `4`)
6. Single letter trailing word (`"hello world a"` → `1`)
7. Massive space gaps between words (`"foo        bar"` → `3`)
8. Long repeated characters in the last word (`"test zzzzzzzzzz"` → `10`)
