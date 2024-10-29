"""
Binary Tree Implementation in Python
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data) -> None:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def __repr__(self) -> str:
        return f"Node: {self.data}"


class Tree:
    def __init__(self) -> None:
        self.root = None
