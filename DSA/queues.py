"""
Queue implementation in Python.
Queue is a data structure that follows the First In First Out (FIFO) principle.
First element inserted into the queue is the first one to be removed.
"""


class Node:
    """
    Creates a node. A node is a single element in a queue.
    The next_node attribute points to the next node in the queue.
    """

    def __init__(self, data=None) -> None:
        self.data = data
        self.next_node = None

    def __repr__(self) -> str:
        """
        Returns a visual representation of the node.
        """
        return f"Node: {self.data}"


class Queue:
    def __init__(self) -> None:
        self.first = None
        self.size = 0

    def enqueue(self, data) -> None:
        """
        Inserts a data in the first of the queue.
        """
        node = Node(data)
        self.size += 1

        if self.first is None:
            self.first = node
        else:
            current = self.first
            while current:
                if current.next_node is None:
                    break
                current = current.next_node
            current.next_node = node

    def dequeue(self) -> None:
        """
        Removes a data in the first of the queue.
        """
        current = self.first
        self.first = current.next_node
        current = None

        self.size -= 1

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty. Returns False otherwise.
        """
        return self.first is None

    def __len__(self) -> int:
        """
        Returns the size of the queue.
        """
        return self.size

    def __repr__(self) -> str:
        """
        Returns a visual representation of the queue.
        """
        current = self.first
        container = ""

        while current:
            container = container + f"{current.data}, "
            if current.next_node is None:
                break
            current = current.next_node

        return f"[{container}]"


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    print(queue)

    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    print(queue)

    queue.dequeue()
    print(queue)

    print(queue.is_empty())

    print(queue.__len__())
