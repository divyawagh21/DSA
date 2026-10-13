# Day 25: Min Stack

- **Problem Link:** [LeetCode #155 - Min Stack](https://leetcode.com/problems/min-stack/)
- **Difficulty:** 🟡 Medium
- **Topic:** Stack
- **Date Solved:** 2026-10-13

---

## 📝 Problem Statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time $O(1)$.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with **$O(1)$ time complexity** for each function.

### Example 1:
```text
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

### Constraints:
- `-2^31 <= val <= 2^31 - 1`
- Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
- At most $3 \times 10^4$ calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## 💡 Algorithmic Approaches

### 1. Single Stack with Linear Search for Min
- Store values in a standard list.
- When `getMin()` is called, compute $\min(stack)$.
- **Time Complexity:** $O(1)$ for push/pop/top, but $O(N)$ for `getMin()` — **violates $O(1)$ requirement**.
- **Space Complexity:** $O(N)$.

### 2. Parallel Min-Stack (Optimal) 🚀
- **Key Insight:** In a stack, elements are added and removed in strict LIFO order. Therefore, the minimum of the stack up to any index $i$ depends only on elements from index $0$ to $i$, and will never change until index $i$ is removed!
- Maintain a second stack: `min_stack`.
  - When pushing `val`, also push $\min(\text{val}, \text{min\_stack}[-1])$ onto `min_stack`.
  - When popping, pop from both `stack` and `min_stack`.
  - `getMin()` simply reads the top element of `min_stack` in $O(1)$ time.
- **Time Complexity:** $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`).
- **Space Complexity:** $O(N)$ auxiliary storage.

---

## 💻 Python Implementation

```python
class MinStack:
    def __init__(self):
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
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

---

## 🔑 Parallel Stack State Trace

```
Operation       Main Stack          Min Stack       Output / Notes
-------------------------------------------------------------------
push(-2)        [-2]                [-2]            -
push(0)         [-2, 0]             [-2, -2]        -
push(-3)        [-2, 0, -3]         [-2, -2, -3]    -
getMin()        [-2, 0, -3]         [-2, -2, -3]    => -3
pop()           [-2, 0]             [-2, -2]        -
top()           [-2, 0]             [-2, -2]        => 0
getMin()        [-2, 0]             [-2, -2]        => -2
```

---

## 🧪 Verification & Test Cases

The solution includes automated unit tests covering:
1. Standard LeetCode example (`[-2, 0, -3]` sequence)
2. Strictly decreasing sequences (min updates on every push and reverts on every pop)
3. Strictly increasing sequences (min stays constant throughout)
4. Duplicate minimum values (validating correct state restoration after duplicate pops)
5. 32-bit extreme signed integer values (`2^31 - 1` and `-2^31`)
