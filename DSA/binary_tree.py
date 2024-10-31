"""
Basic Binary Tree Implementation in Python
"""


class TreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data) -> None:
        """
        Inserts a node at the left or right of the root tree.
        Self balancing.
        """
        if self.left is None:
            self.left = TreeNode(data)
        elif self.right is None:
            self.right = TreeNode(data)
        elif self.left.left is not None:
            self.right.insert(data)
        else:
            self.left.insert(data)

    def tree_traversal(self) -> None:
        """
        Displays the nodes of the tree from bottom-up, leftmost node first.
        """
        if self.left is not None:
            self.left.tree_traversal()

        print(self.data)

        if self.right is not None:
            self.right.tree_traversal()


# Test case.
if __name__ == "__main__":
    tree = TreeNode(1)

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    tree.tree_traversal()
