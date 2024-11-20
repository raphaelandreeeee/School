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
        Inserts a node to the left of the root node if it does not exist. inserts a node to the right of the node, otherwise. Recursively inserts if both nodes are not empty.
        """
        
        if self.data > data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def inorder_traversal(self) -> list:
        """
        Traverses the tree in ascending order.
        """
        
        container = []

        if self.left is not None:
            container.extend(self.left.inorder_traversal())
        
        container.append(self.data)
        
        if self.right is not None:
            container.extend(self.right.inorder_traversal())

        return container
    
    def preorder_traversal(self) -> list:
        """
        Traverses the tree from to root node to the left subtree then finally to the right subtree.
        """
        
        container = []

        container.append(self.data)
        
        if self.left is not None:
            container.extend(self.left.preorder_traversal())
        
        if self.right is not None:
            container.extend(self.right.preorder_traversal())

        return container

    def postorder_traversal(self) -> list:
        """
        Traverses the tree from the left subtree to the right subtree then finally to the root node.
        """
        
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

    dataset = [10, 20, 40, 50,]
    for data in dataset:
        tree.insert(data)

    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())