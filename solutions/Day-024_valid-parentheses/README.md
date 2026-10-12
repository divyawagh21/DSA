# Day 24: Valid Parentheses

- **Problem Link:** [LeetCode #20 - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- **Difficulty:** 🟢 Easy
- **Topic:** Stack
- **Date Solved:** 2026-10-12

---

## 📝 Problem Statement

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Example 1:
```text
Input: s = "()"
Output: true
```

### Example 2:
```text
Input: s = "()[]{}"
Output: true
```

### Example 3:
```text
Input: s = "(]"
Output: false
```

### Example 4:
```text
Input: s = "([])"
Output: true
```

### Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'()[]{}'`.

---

## 💡 Algorithmic Approaches

### 1. String Replacement (Naive)
- Repeatedly replace `"()"`, `"{}"`, and `"[]"` with `""` until no occurrences remain.
- If the final string is empty, return `true`; else `false`.
- **Time Complexity:** $O(N^2)$ — Each replacement requires string copies.
- **Space Complexity:** $O(N)$ for intermediate strings.

### 2. Stack (Optimal) 🚀
- **Key Insight:** Brackets follow a symmetric Last-In-First-Out (LIFO) pattern. The most recently opened bracket must be the first to be closed.
- **Algorithm:**
  1. If `len(s) % 2 != 0`, immediately return `false` (odd-length strings cannot be balanced).
  2. Map each closing bracket to its corresponding opening bracket: `matching = {')': '(', '}': '{', ']': '['}`.
  3. Iterate through characters in `s`:
     - If closing bracket: verify stack is non-empty and top element equals `matching[char]`. Pop it.
     - If opening bracket: push onto stack.
  4. At the end, return `len(stack) == 0`.
- **Time Complexity:** $O(N)$ — Single pass over string.
- **Space Complexity:** $O(N)$ — Stack stores at most $N$ elements.

---

## 💻 Python Implementation

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        matching = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in matching:
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
```

---

## 🔑 Stack Lifecycle Trace

```
s = " ( [ ] ) "

char = '(' : stack = ['(']
char = '[' : stack = ['(', '[']
char = ']' : matches top '[', pop -> stack = ['(']
char = ')' : matches top '(', pop -> stack = []

End: stack is empty -> return True ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Simple pair (`"()"` → `True`)
2. Sequential bracket pairs (`"()[]{}"` → `True`)
3. Mismatched bracket types (`"(]"` → `False`)
4. Nested brackets (`"([])"` → `True`)
5. Deeply nested valid brackets (`"{[()()]}"` → `True`)
6. Odd length string (`"([)"` → `False`)
7. Unclosed opening brackets (`"((("` → `False`)
8. Unmatched closing brackets (`")))"` → `False`)
9. Closing bracket appears first (`")("` → `False`)
10. Interleaved invalid sequence (`"([)]"` → `False`)
