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

    def delete(self, data):
        if self is None:
            return self

        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            temp = self.right.minimum()
            self.data = temp.data
            self.right = self.right.delete(temp.data)

        return self

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


if __name__ == '__main__':
    tree = TreeNode(88)

    dataset = [5, 7, 15, 17, 22, 23, 32, 34, 36, 37, 38, 60, 72, 78, 86, 88, 89, 90]

    for data in dataset:
        tree.insert(data)

    print(tree.inorder_traversal())

    tree.delete(34)

    print(tree.search(23))

    print(tree.minimum())
    print(tree.maximum())

    print(tree.successor(23))
    print(tree.predeccessor(23))
    
    print(tree.inorder_traversal())
    print(tree.preorder_traversal())
    print(tree.postorder_traversal())
    