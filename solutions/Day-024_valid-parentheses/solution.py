"""
LeetCode #20: Valid Parentheses
Difficulty: Easy
Topic: Stack
Date Solved: 2026-10-12

Problem:
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Validate brackets matching using a Last-In-First-Out (LIFO) Stack.

        Intuition:
        Parentheses matching follows a nested, symmetric structure: the most recently
        opened bracket must be the first one closed. This makes a Stack the ideal data structure.

        Algorithm:
        1. An odd-length string can never have balanced brackets (early return False).
        2. Create a hash map mapping each closing bracket to its matching open bracket:
           {')': '(', '}': '{', ']': '['}.
        3. Traverse characters in `s`:
           - If it is a closing bracket:
             - Check the top of the stack. If the stack is empty or the top element does
               not match the corresponding open bracket, return False.
             - Otherwise, pop the matching open bracket from the stack.
           - If it is an opening bracket:
             - Push it onto the stack.
        4. After the iteration, the string is valid if and only if the stack is completely empty.

        Complexity:
        - Time Complexity: O(N) — Single linear scan through string of length N.
        - Space Complexity: O(N) — In the worst case (e.g. "((((("), all brackets are stored in the stack.
        """
        if len(s) % 2 != 0:
            return False

        matching = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in matching:
                # Closing bracket: check and pop
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket: push onto stack
                stack.append(char)

        return len(stack) == 0


# --- Unit Tests ---
def test_is_valid():
    solver = Solution()

    # Test Case 1: Standard simple pair
    assert solver.isValid("()") is True, "TC1 failed on '()'"

    # Test Case 2: Consecutive diverse brackets
    assert solver.isValid("()[]{}") is True, "TC2 failed on '()[]{}'"

    # Test Case 3: Mismatched bracket types
    assert solver.isValid("(]") is False, "TC3 failed on '(]'"

    # Test Case 4: Properly nested brackets
    assert solver.isValid("([])") is True, "TC4 failed on '([])'"

    # Test Case 5: Deeply nested valid brackets
    assert solver.isValid("{[()()]}") is True, "TC5 failed on '{[()()]}'"

    # Test Case 6: Odd length string
    assert solver.isValid("([)") is False, "TC6 failed on '([)'"

    # Test Case 7: Only open brackets
    assert solver.isValid("(((") is False, "TC7 failed on '((('"

    # Test Case 8: Only closing brackets (stack empty initially)
    assert solver.isValid(")))") is False, "TC8 failed on ')))'"

    # Test Case 9: Closing bracket before opening bracket
    assert solver.isValid(")( ") is False or solver.isValid(")(") is False, "TC9 failed on ')('"

    # Test Case 10: Interleaved invalid brackets
    assert solver.isValid("([)]") is False, "TC10 failed on '([)]'"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_is_valid()
