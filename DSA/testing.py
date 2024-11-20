class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_data_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def min_data_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, data):
        if not root or root.data == data:
            return root
        if root.data < data:
            return self.search(root.right, data)
        return self.search(root.left, data)

    def insert_data(self, data):
        self.root = self.insert(self.root, data)

    def delete_data(self, data):
        self.root = self.delete(self.root, data)

    def search_data(self, data):
        return self.search(self.root, data)
    

def inorder_traversal(root):
    container = []

    def _inorder_traversal(node):
        if node:
            _inorder_traversal(node.left)
            container.append(node.data)
            _inorder_traversal(node.right)

    _inorder_traversal(root)
    return container

# Example usage:
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_data(10)
    tree.insert_data(20)
    tree.insert_data(30)
    tree.insert_data(40)
    tree.insert_data(50)

    print(inorder_traversal(tree.root))

    tree.delete_data(20)
    print(inorder_traversal(tree.root))

    result = tree.search_data(30)
    if result:
        print("Node found")
    else:
        print("Node not found")
