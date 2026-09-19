# Day 03: Valid Anagram

- **Problem Link:** [LeetCode #242 - Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- **Difficulty:** 🟢 Easy
- **Topic:** Arrays & Hashing
- **Date Solved:** 2026-09-19

---

## 📝 Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
```text
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2:
```text
Input: s = "rat", t = "car"
Output: false
```

### Constraints:
- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

### Follow-up:
What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

## 💡 Algorithmic Approaches

### 1. Sorting Approach
- Sort both strings alphabetically: `sorted(s) == sorted(t)`.
- If both sorted sequences are equal, they contain the identical multiset of characters.
- **Time Complexity:** $O(N \log N)$ where $N$ is the length of the strings due to comparison sorting (Timsort).
- **Space Complexity:** $O(N)$ or $O(1)$ depending on whether string sorting generates intermediate copies.

### 2. Hash Map / Frequency Array (Optimal) 🚀
- **Step 1:** Check if `len(s) != len(t)`. If their lengths differ, they cannot be anagrams — immediately return `false`.
- **Step 2:** Maintain a fixed-size frequency table of 26 integers for lowercase English letters (or a dictionary/hash map for arbitrary Unicode characters).
- **Step 3:** Iterate through both strings simultaneously:
  - Increment the count for each character from `s`.
  - Decrement the count for each character from `t`.
- **Step 4:** Check if every bucket in the frequency table is `0`. If any count is non-zero, return `false`. Otherwise, return `true`.
- **Time Complexity:** $O(N)$ linear time, since we process each character in a single pass.
- **Space Complexity:** $O(1)$ auxiliary space, since the table size is strictly bounded to 26 characters (or $O(K)$ distinct characters for Unicode).

---

## 💻 Python Implementation

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26

        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord("a")] += 1
            count[ord(char_t) - ord("a")] -= 1

        return all(c == 0 for c in count)
```

---

## 🧪 Verification & Test Cases

The solution includes automated unit tests covering:
1. Standard valid anagrams (`"anagram"` vs `"nagaram"`)
2. Standard invalid anagrams (`"rat"` vs `"car"`)
3. Mismatched string lengths (`"a"` vs `"ab"`)
4. Single character identical matches (`"z"` vs `"z"`)
5. Single character mismatches (`"a"` vs `"b"`)
6. Identical character sets with differing counts (`"aacc"` vs `"ccac"`)
7. Real-world anagram pairs (`"listen"` vs `"silent"`)
8. Uniform character repetitions (`"aaaaaa"` vs `"aaaaaa"`)
