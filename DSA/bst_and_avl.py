"""
Binary Search Tree Implementation in Python
"""

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __contains__(self, data) -> bool:
        if data not in self.inorder_traversal():
            return False
        return True
    
    def __repr__(self) -> str:
        return str(self.data)

    def search(self, data) -> None:
        if self.data == data:
            return self
        elif self.data > data and self.left is not None:
            return self.left.search(data)
        elif self.data < data and self.right is not None:
            return self.right.search(data)
        else:
            return None

    def minimum(self) -> int:
        current = self.left

        while current is not None:
            if current.left is None:
                break
            current = current.left
        
        return current.data

    def maximum(self) -> int:
        current = self.right

        while current is not None:
            if current.right is None:
                break
            current = current.right
        
        return current.data
    
    def successor(self, data) -> int:
        if self.data == data:
            return self.right
        elif self.data < data and self.right is not None:
            return self.right.successor(data)

    def predeccessor(self, data) -> int:
        if self.data == data:
            return self.left
        elif self.data > data and self.left is not None:
            return self.right.predeccessor(data)

    def insert(self, data) -> None:
        """
        Adds a node to the tree.
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

    def delete(self, data) -> None:
        pass

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


class AVL(TreeNode):
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 1

    def _height(self, node) -> int:
        if node is None:
            return 0
        return node.height
    
    def _balance(self, node) -> int:
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)
    
    def _left_rotate(self, node) -> TreeNode:
        node_right = node.right
        tree = node_right.left
        node_right.left = node
        node.right = tree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node_right.height = 1 + max(self._height(node_right.left), self._height(node_right.right))

    def _right_rotate(self, node) -> TreeNode:
        node_left = node.left
        tree = node_left.right
        node_left.right = node
        node.left = tree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node_left.height = 1 + max(self._height(node_left.left), self._height(node_left.right))

    def insert(self, node, data) -> None:
        if node is None:
            return TreeNode(data)
        
        if data < self.data:
            node.left = self.insert(node.left, data)
        elif data > self.data:
            node.right = self.insert(node.right, data)

        # Updates the balance and height.
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        self.balance = self._balance(node)

        # Balancing the tree.
        # Left left case.
        if self.balance > 1 and self._balance(node.left) >= 0:
            return self._right_rotate(node)
        
        # Left right case.
        if self.balance > 1 and self._balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        
        # Right right case.
        if self.balance < 1 and self._balance(node.right) >= 0:
            return self._left_rotate(node)
        
        # Right left case.
        if self.balance < 1 and self._balance(node.right) < 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)


if __name__ == '__main__':
    tree = TreeNode(30)

    tree.insert(10)
    tree.insert(20)
    tree.insert(40)
    tree.insert(50)

    print(tree.search(20))

    print(tree.minimum())
    print(tree.maximum())

    print(tree.successor(30))
    print(tree.predeccessor(30))

    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())

    print(f"\nAVL Tree\n")

    avl = AVL(30)

    array = [10, 20, 30, 40]
    for data in array:
        avl.insert(avl, array)

    print(avl.inorder_traversal())