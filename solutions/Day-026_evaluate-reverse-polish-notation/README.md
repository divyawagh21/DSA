# Day 26: Evaluate Reverse Polish Notation

- **Problem Link:** [LeetCode #150 - Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)
- **Difficulty:** 🟡 Medium
- **Topic:** Stack
- **Date Solved:** 2026-10-14

---

## 📝 Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in **Reverse Polish Notation** (postfix notation).

Evaluate the expression. Return an integer that represents the value of the expression.

**Note that:**
- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always **truncates toward zero**.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

### Example 1:
```text
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2:
```text
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3:
```text
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

### Constraints:
- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

---

## 💡 Algorithmic Approaches

### 1. Stack Evaluation (Optimal) 🚀
- In Reverse Polish Notation, every operator immediately acts on the **two most recently evaluated operands**.
- A **LIFO Stack** naturally models this behavior:
  1. Iterate through `tokens` sequentially.
  2. If the token is a number: parse it to integer and push onto the stack.
  3. If the token is an operator:
     - Pop the top element as `b` (right operand).
     - Pop the next element as `a` (left operand).
     - Calculate `a op b` and push the result back onto the stack.
  4. After traversing all tokens, the final result is the single remaining number in the stack.

### ⚠️ Python Floor Division Pitfall
- In Python, `//` rounds toward $-\infty$ (e.g. `-7 // 3 = -3` and `6 // -132 = -1`).
- The problem strictly mandates **truncation toward zero** (e.g. `int(-7 / 3) = -2` and `int(6 / -132) = 0`).
- Using `int(a / b)` correctly truncates toward zero for all positive and negative numbers.

### Complexity:
- **Time Complexity:** $O(N)$ — Each token is pushed and popped at most once.
- **Space Complexity:** $O(N)$ — Stack holds intermediate operand values.

---

## 💻 Python Implementation

```python
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # Truncates toward zero
        }

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]
```

---

## 🔑 RPN Evaluation Trace

```
tokens = ["4", "13", "5", "/", "+"]

token = "4"  : stack = [4]
token = "13" : stack = [4, 13]
token = "5"  : stack = [4, 13, 5]
token = "/"  : b = 5, a = 13 -> int(13 / 5) = 2 -> stack = [4, 2]
token = "+"  : b = 2, a = 4  -> 4 + 2 = 6        -> stack = [6]

Final Result: 6 ✓
```

---

## 🧪 Verification & Test Cases

The solution includes 10 automated unit tests:
1. Standard addition and multiplication (`((2 + 1) * 3) = 9`)
2. Division followed by addition with positive truncation (`(4 + (13 / 5)) = 6`)
3. Complex nested expression (`22`)
4. Negative division truncating to zero (`6 / -132 = 0`)
5. Negative result from subtraction (`3 - 5 = -2`)
6. Single token boundary case (`["42"]` → `42`)
7. Negative division yielding negative integer (`7 / -3 = -2`)
8. Zero numerator in division (`0 / 3 = 0`)
9. Sequential subtractions verifying operand ordering (`15 - 5 - 2 = 8`)
10. Multiplying two negative integers (`-3 * -4 = 12`)
