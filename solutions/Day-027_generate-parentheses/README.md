# Day 27: Generate Parentheses

- **Problem Link:** [LeetCode #22 - Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- **Difficulty:** 🟡 Medium
- **Topic:** Stack
- **Date Solved:** 2026-10-15

---

## 📝 Problem Statement

Given `n` pairs of parentheses, write a function to generate all combinations of **well-formed parentheses**.

### Example 1:
```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2:
```text
Input: n = 1
Output: ["()"]
```

### Constraints:
- `1 <= n <= 8`

---

## 💡 Algorithmic Approaches

### 1. Brute Force (Generate All $2^{2n}$ Sequences)
- Generate all possible combinations of `'('` and `')'` of length $2n$.
- Validate each using the Day 24 `isValid` check.
- **Time Complexity:** $O(2^{2n} \cdot n)$ — Explores vast numbers of invalid sequences.
- **Space Complexity:** $O(n)$.

### 2. Backtracking with Stack Pruning (Optimal) 🚀
- **Key Insight:** Build only valid prefixes by maintaining explicit counts of open and closed brackets:
  1. Add `'('` if `open_count < n`.
  2. Add `')'` only if `close_count < open_count` (cannot close an unopened bracket).
  3. Base case: When `open_count == close_count == n`, append the current stack string to the results.
- **Pruning power:** Never explores an invalid branch. The number of valid combinations generated equals the $n$-th **Catalan Number**:
  $$C_n = \frac{1}{n+1}\binom{2n}{n}$$
  For $n = 1, 2, 3, 4$, $C_n = 1, 2, 5, 14$.

### Complexity:
- **Time Complexity:** $O(\frac{4^n}{\sqrt{n}})$ — Asymptotically bounded by $C_n$.
- **Space Complexity:** $O(n)$ — Stack recursion depth is at most $2n$.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_count: int, close_count: int):
            if open_count == close_count == n:
                result.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)
        return result
```

---

## 🔑 Decision Tree Visualization ($n = 2$)

```
                   "" (0,0)
                  /
                "(" (1,0)
               /        \
          "((" (2,0)     "()" (1,1)
            |               |
          "(()" (2,1)     "()(" (2,1)
            |               |
         "(())" (2,2)     "()()" (2,2)
           ✓                ✓
```

---

## 🧪 Verification & Test Cases

The solution includes automated unit tests covering:
1. $n = 1$ ($C_1 = 1 \rightarrow \text{["()"]}$)
2. $n = 2$ ($C_2 = 2 \rightarrow \text{["(())", "()()"]}$)
3. $n = 3$ ($C_3 = 5$ standard LeetCode example)
4. $n = 4$ ($C_4 = 14$ combinatorial verification and uniqueness check)
5. Comprehensive bracket validity assertion on all generated outputs
