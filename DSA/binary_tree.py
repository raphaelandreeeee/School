"""
Basic Binary Tree Implementation in Python
"""


class TreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add(self, data) -> None:
        if self.data > data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add(data)

    def inorder_traversal(self) -> list:
        container = []

        if self.left is not None:
            container.extend(self.left.inorder_traversal())
        
        container.append(self.data)
        
        if self.right is not None:
            container.extend(self.right.inorder_traversal())

        return container
    
    def preorder_traversal(self) -> list:
        container = []

        container.append(self.data)
        
        if self.left is not None:
            container.extend(self.left.preorder_traversal())
        
        if self.right is not None:
            container.extend(self.right.preorder_traversal())

        return container

    def postorder_traversal(self) -> list:
        container = []

        if self.left is not None:
            container.extend(self.left.postorder_traversal())
        
        if self.right is not None:
            container.extend(self.right.postorder_traversal())

        container.append(self.data)
        
        return container

# Test case.
if __name__ == "__main__":
    tree = TreeNode(30)

    tree.add(10)
    tree.add(20)
    tree.add(40)
    tree.add(50)

    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())
