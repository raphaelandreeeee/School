"""
Stack implementation in Python
Stack is a data structure that follows the Last In First Out (LIFO) principle.
Last element inserted into the stack is the first one to be removed.
"""


class Node:
    """
    Creates a node. A node is a single element in a stack.
    The next_node attribute points to the next node in the stack.
    """

    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        """
        Returns a visual representation of the node.
        """
        return f"Node: {self.data}"


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.next = None
        self.size = 0

    def push(self, data) -> None:
        """
        Inserts a data on the top of the stack.
        """
        node = Node(data)
        self.size += 1

        if self.top is None:
            self.top = node
        else:
            node.next_node = self.top
            self.top = node

    def pop(self) -> any:
        """
        Removes and returns the top item on the stack.
        """
        item = self.top
        new_top = item.next_node
        self.top = new_top

        self.size -= 1

        return item.data

    def peek(self) -> any:
        """
        Returns the top item on the stack.
        """
        return self.top.data

    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty. Returns False otherwise.
        """
        return self.top is None

    def __repr__(self) -> str:
        """
        Returns the visual representation of the stack.
        """
        current = self.top
        container = ""

        while current:
            container = f"{current.data}, " + container
            if current.next_node is None:
                break
            current = current.next_node

        return f"[{container}]"

    def __len__(self) -> int:
        """
        Returns the size of the stack.
        """
        return self.size


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    print(stack)

    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(stack)

    item = stack.pop()
    print(stack, item)

    print(stack.peek())

    print(stack.__len__())
