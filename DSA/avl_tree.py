"""
Binary Search Tree Implementation in Python
"""


class AVLTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def _get_height(self, node) -> int:
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node) -> int:
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _left_rotate(self, node) -> "AVLTree":
        node_right = node.right
        tree = node_right.left
        node_right.left = node
        node.right = tree

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node_right.height = 1 + max(self._get_height(node_right.left), self._get_height(node_right.right))

        return node_right

    def _right_rotate(self, node) -> "AVLTree":
        node_left = node.left
        tree = node_left.right
        node_left.right = node
        node.left = tree

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node_left.height = 1 + max(self._get_height(node_left.left), self._get_height(node_left.right))

        return node_left

    def insert(self, node, data) -> None:
        if node is None:
            return AVLTree(data)
        
        if data < self.data:
            node.left = self.insert(node.left, data)
        elif data > self.data:
            node.right = self.insert(node.right, data)

        # Updates the balance and height.
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        # Balancing the tree.
        # Left left case.
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        
        # Left right case.
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right right case.
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        # Right left case.
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

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
    

if __name__ == '__main__':
    tree = AVLTree(30)

    dataset = [10, 20, 40, 50, 60, 70, 80, 90]

    for data in dataset:
        tree = tree.insert(tree, data)

    print(tree.inorder_traversal())