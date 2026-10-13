"""
LeetCode #155: Min Stack
Difficulty: Medium
Topic: Stack
Date Solved: 2026-10-13

Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time O(1).

Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""


class MinStack:
    def __init__(self):
        """
        Initialize the main stack and a parallel min_stack.

        Intuition:
        In a standard stack, retrieving the minimum element takes O(N) because we
        would have to inspect every item.

        To achieve O(1) retrieval for getMin():
        We maintain a parallel `min_stack` where `min_stack[i]` records the minimum
        value present in the stack from index 0 up to index i.
        - Whenever a new value is pushed, we push `min(val, current_min)` onto `min_stack`.
        - Whenever an element is popped from the main stack, we also pop from `min_stack`.
        - Thus, `min_stack[-1]` always points to the minimum element of the current stack state in O(1) time.

        Complexity:
        - Time Complexity:
          - push: O(1)
          - pop: O(1)
          - top: O(1)
          - getMin: O(1)
        - Space Complexity: O(N) — Parallel stack holds at most N elements.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("top from empty MinStack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("getMin from empty MinStack")


# --- Unit Tests ---
def test_min_stack():
    # Test Case 1: LeetCode Example 1
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3, "TC1 failed: getMin after push(-3) should be -3"
    min_stack.pop()
    assert min_stack.top() == 0, "TC1 failed: top after pop should be 0"
    assert min_stack.getMin() == -2, "TC1 failed: getMin after pop should revert to -2"

    # Test Case 2: Strictly decreasing elements
    s2 = MinStack()
    s2.push(5)
    s2.push(4)
    s2.push(3)
    s2.push(2)
    s2.push(1)
    assert s2.getMin() == 1, "TC2 failed on strictly decreasing push"
    s2.pop()
    assert s2.getMin() == 2, "TC2 failed on first pop"
    s2.pop()
    assert s2.getMin() == 3, "TC2 failed on second pop"

    # Test Case 3: Strictly increasing elements
    s3 = MinStack()
    s3.push(10)
    s3.push(20)
    s3.push(30)
    assert s3.getMin() == 10, "TC3 failed: min should stay 10"
    assert s3.top() == 30, "TC3 failed: top should be 30"
    s3.pop()
    assert s3.getMin() == 10, "TC3 failed: min should remain 10 after pop"

    # Test Case 4: Duplicate minimum elements
    s4 = MinStack()
    s4.push(2)
    s4.push(0)
    s4.push(3)
    s4.push(0)
    assert s4.getMin() == 0, "TC4 failed: min should be 0"
    s4.pop()
    assert s4.getMin() == 0, "TC4 failed: min should still be 0 after popping duplicate"
    s4.pop()
    assert s4.getMin() == 0, "TC4 failed: min should still be 0"
    s4.pop()
    assert s4.getMin() == 2, "TC4 failed: min should revert to 2 after original 0 popped"

    # Test Case 5: Negative numbers with extreme integer values
    s5 = MinStack()
    s5.push(2147483647)
    s5.push(-2147483648)
    assert s5.getMin() == -2147483648, "TC5 failed on INT_MIN"
    assert s5.top() == -2147483648, "TC5 failed on top"
    s5.pop()
    assert s5.getMin() == 2147483647, "TC5 failed on revert to INT_MAX"

    print("All unit tests passed successfully!")


if __name__ == "__main__":
    test_min_stack()
