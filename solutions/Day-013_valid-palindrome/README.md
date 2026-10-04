# Day 13: Valid Palindrome

- **Problem Link:** [LeetCode #125 - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **Difficulty:** 🟢 Easy
- **Topic:** Two Pointers
- **Date Solved:** 2026-10-04

---

## 📝 Problem Statement

A phrase is a **palindrome** if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example 1:
```text
Input:  s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:
```text
Input:  s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:
```text
Input:  s = " "
Output: true
Explanation: After removing non-alphanumeric chars, s is empty → palindrome.
```

### Constraints:
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

---

## 💡 Algorithmic Approaches

### 1. Clean Then Compare
- Filter to alphanumeric + lowercase, then check `cleaned == cleaned[::-1]`.
- **Time:** $O(N)$ | **Space:** $O(N)$ — creates an intermediate cleaned string.

### 2. Two Pointers In-Place (Optimal) 🚀
- Place `left` at index 0 and `right` at index `len(s) - 1`.
- **Skip** non-alphanumeric characters by advancing each pointer inward.
- **Compare** `s[left].lower()` vs `s[right].lower()`.
  - Mismatch → return `False`.
  - Match → move both pointers inward.
- When `left >= right`, all characters matched → return `True`.
- **Time Complexity:** $O(N)$ — each character is visited at most once.
- **Space Complexity:** $O(1)$ — only two integer pointers, no cleaned copy.

---

## 💻 Python Implementation

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

---

## 🔑 Two-Pointer Trace

```
s = "A man, a plan, a canal: Panama"

left →  A m a n , ← skip comma → a ...
right → a m a n a P : ← skip colon/space → a ...

Step 1: s[0]='A' vs s[29]='a' → 'a'=='a' ✓ → move inward
Step 2: s[1]=' ' → skip; s[28]='m' → compare...
...
All characters match → True ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 11 automated unit tests:
1. LeetCode Example 1 — classic phrase palindrome
2. LeetCode Example 2 — not a palindrome
3. Single space — empty after filtering → `True`
4. Single character → `True`
5. Two identical characters → `True`
6. Two different characters → `False`
7. Mixed digit and letter, not palindrome
8. Pure digit palindrome `"12321"`
9. Mixed alphanumeric palindrome `"A1 1a"`
10. All non-alphanumeric → empty → `True`
11. Long classic palindrome sentence
