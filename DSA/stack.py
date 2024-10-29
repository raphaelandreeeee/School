"""
Stack implementation in Python
Stack is a data structure that follows the Last In First Out (LIFO) principle.
Last element inserted into the stack is the first one to be removed.
"""


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        """
        Adds an element to the top of the stack.
        """
        self.stack = self.stack + [data]

    def pop(self) -> None:
        """
        Removes the top element from the stack. 
        """
        if self.stack:
            del self.stack[-1]
        else:
            self.stack = []

    def __repr__(self) -> str:
        """
        Returns a visual representation of the stack.
        """
        return f"Stack: {self.stack}"


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)                    # Output: Stack: [3, 2, 1]

    stack.pop()
    print(stack)                    # Output: Stack: [2, 1]

    stack.pop()
    print(stack)                    # Output: Stack: [1]

    stack.pop()
    print(stack)                    # Output: Stack: []
