"""
Linked List in Python
"""


class Node:
    """
    Creates a node. A node is a single element in a linked list.
    The next_node attribute points to the next node in the linked list.
    """

    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        """
        Returns a visual representation of the node.
        """
        return f"Node: {self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, data) -> None:
        """
        Appends a node to the end of the linked list.
        """
        node = Node(data)
        self.size += 1

        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node

    def prepend(self, data) -> None:
        """
        Appends a node to the start of the linked list.
        """

        node = Node(data)
        self.size += 1

        node.next_node = self.head
        self.head = node

    def insert(self, index, data) -> None:
        """
        Inserts a node at the specified index in the linked list.
        """
        current = self.head
        self.size += 1

        if index == 0:
            self.prepend(data)
        else:
            node = Node(data)
            for i in range(index - 1):
                current = current.next_node

            if current is None:
                raise IndexError("Index out of bounds.")
            else:
                node.next_node = current.next_node
                current.next_node = node

    def delete(self, data) -> None:
        """
        Deletes a data in the linked list.
        """
        current = self.head
        self.size -= 1

        if current.data == data:
            self.head = current.next_node
            current = None
        else:
            while current.next_node:
                if current.next_node.data == data:
                    current.next_node = current.next_node.next_node
                    break
                current = current.next_node

    def pop(self, index) -> None:
        """
        Deletes a data at a specified index in the linked list.
        """
        if self.head is None:
            raise IndexError("Index out of bounds.")
        else:
            current = self.head
            self.size -= 1

        if index == 0:
            self.head = current.next_node
            current = None
        else:
            for i in range(index - 1):
                if current.next_node is None:
                    raise IndexError("Index out of bounds.")
                current = current.next_node

            if current.next_node is None:
                raise IndexError("Index out of bounds.")
            else:
                current.next_node = current.next_node.next_node

    def __contains__(self, data) -> bool:
        """
        Returns True if the specified data is in the linked list. Returns False otherwise.
        """
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next_node
        return False

    def __len__(self) -> int:
        """
        Returns the length of the linked list.
        """
        return self.size

    def __repr__(self) -> str:
        """
        Returns a visual representation of the linked list.
        You can use a display method to print the linked list but using a representation dunder method is more formal.
        """
        l = []
        current = self.head

        if current.next_node is None:
            return f"Head: {current.data}"

        while current is not None:
            if current == self.head:
                l.append(f"Head: {current.data}")
            elif current.next_node is None:
                l.append(f"Tail: {current.data}")
                break
            else:
                l.append(f"{current}")
            current = current.next_node

        return "-> ".join(l)


# Test the linked list.
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)

    print(linked_list)

    linked_list.prepend(50)

    print(linked_list)

    linked_list.insert(5, 100)

    print(linked_list)

    linked_list.delete(10)

    print(linked_list)

    linked_list.pop(1)

    print(linked_list)
    print(linked_list.__len__())
