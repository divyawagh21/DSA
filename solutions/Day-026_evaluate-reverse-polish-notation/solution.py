"""
LeetCode #150: Evaluate Reverse Polish Notation
Difficulty: Medium
Topic: Stack
Date Solved: 2026-10-14

Problem:
You are given an array of strings `tokens` that represents an arithmetic expression
in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate arithmetic expression in Reverse Polish Notation (Postfix) using a Stack.

        Intuition:
        In Reverse Polish Notation (RPN), operators follow their operands.
        For example: `["2", "1", "+"]` means `2 + 1`.
        
        Because operators always apply to the two most recently evaluated operands,
        a LIFO Stack is the optimal data structure:
        - When encountering an operand (number), push it onto the stack.
        - When encountering an operator (`+`, `-`, `*`, `/`), pop the two most recent
          operands: the first popped is the right operand `b`, the second is the left operand `a`.
        - Apply the operation: `a op b`, and push the result back onto the stack.

        Important Truncation-Toward-Zero Note:
        In Python, integer division `a // b` is floor division (e.g. -7 // 3 = -3).
        However, the problem requires truncation toward zero (-7 / 3 truncated is -2).
        Using `int(a / b)` achieves exact truncation toward zero for both positive and negative values.

        Complexity:
        - Time Complexity: O(N) — Every token is processed once in linear time.
        - Space Complexity: O(N) — Stack stores at most N operands.
        """
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
                result = operators[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


# --- Unit Tests ---
def test_eval_rpn():
    solver = Solution()

    # Test Case 1: Simple addition and multiplication
    # ((2 + 1) * 3) = 9
    assert solver.evalRPN(["2", "1", "+", "3", "*"]) == 9, "TC1 failed"

    # Test Case 2: Division and addition with positive truncation
    # (4 + (13 / 5)) = (4 + 2) = 6
    assert solver.evalRPN(["4", "13", "5", "/", "+"]) == 6, "TC2 failed"

    # Test Case 3: Complex multi-operator expression from LeetCode
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert solver.evalRPN(tokens3) == 22, "TC3 failed"

    # Test Case 4: Negative division truncation toward zero
    # 6 / -132 = 0 (not -1)
    assert solver.evalRPN(["6", "-132", "/"]) == 0, "TC4 failed: negative division should truncate to 0"

    # Test Case 5: Negative result from subtraction
    assert solver.evalRPN(["3", "5", "-"]) == -2, "TC5 failed: 3 - 5 should be -2"

    # Test Case 6: Single operand (no operators)
    assert solver.evalRPN(["42"]) == 42, "TC6 failed on single token"

    # Test Case 7: Negative division yielding negative integer
    # 7 / -3 = -2 (truncated toward zero)
    assert solver.evalRPN(["7", "-3", "/"]) == -2, "TC7 failed on 7 / -3"

    # Test Case 8: Multiplication by zero
    assert solver.evalRPN(["0", "3", "/"]) == 0, "TC8 failed on 0 / 3"

    # Test Case 9: Consecutive subtractions (checking operand order)
    # 15 - 5 - 2 = (15 - 5) - 2 = 10 - 2 = 8
    assert solver.evalRPN(["15", "5", "-", "2", "-"]) == 8, "TC9 failed"

    # Test Case 10: Mixed positive and negative multiplication
    assert solver.evalRPN(["-3", "-4", "*"]) == 12, "TC10 failed on (-3 * -4)"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_eval_rpn()
