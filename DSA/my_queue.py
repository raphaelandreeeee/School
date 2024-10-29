"""
Queue implementation in Python.
Queue is a data structure that follows the First In First Out (FIFO) principle.
First element inserted into the queue is the first one to be removed.
"""


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data) -> None:
        """
        Adds an element to the end of the queue.
        """
        self.queue = self.queue + [data]

    def dequeue(self) -> None:
        """
        Removes the first element from the queue.
        """
        if not self.is_empty():
            del self.queue[0]

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.
        """
        return not self.queue

    def __repr__(self) -> str:
        """
        Returns a visual representation of the queue.
        """
        return f"Queue: {self.queue}"


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)                    # Output: Queue: [1, 2, 3]

    queue.dequeue()
    print(queue)                    # Output: Queue: [2, 3]

    queue.dequeue()
    print(queue)                    # Output: Queue: [3]

    queue.dequeue()
    print(queue)                    # Output: Queue: []z
    print(queue.is_empty())         # Output: True
