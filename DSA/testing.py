from DSA.stack import Stack
from my_queue import Queue


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack)

    stack.pop()
    print(stack)

    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)

    queue.dequeue()
    print(queue)


main()
