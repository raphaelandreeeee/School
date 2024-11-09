class Node:

    def __init__(self, name, concern) -> None:
        self.name = name
        self.concern = concern
        self.next = None

    def __repr__(self) -> None:
        return (self.name, self.concern)
    

class MyQueue:

    def __init__(self) -> None:
        self.first = None
        self.size = 0

    def enqueue(self, name, concern) -> None:
        """
        Prepends the person on the queue.
        """
        
        new_node = Node(name, concern)
        self.size += 1
        current = self.first

        if current is None:
            self.first = new_node
        else:
            while current is not None:
                if current.next is None:
                    break
                current = current.next

            current.next = new_node

    def enter_room(self) -> str:
        """
        Peeks the first person on the queue.
        """
        
        return f"{self.first.name} is entering the room."
    
    def begin_consultation(self) -> str:
        """
        Pops the first person on the queue.
        """
        
        name = self.first.name
        concern = self.first.concern

        current = self.first
        self.first = current.next
        current = None

        self.size -= 1

        return f"{name}'s concern is {concern}."
    
    def closing_time(self) -> None:
        """
        Returns and deletes the whole queue.
        """
        
        self.first.next = None
        self.first = None
        self.size = 0

    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty. Returns False, otherwise.
        """
        
        return self.size == 0
    

if __name__ == '__main__':
    queue = MyQueue()

    # Console loop.
    while True:
        # User input loop.
        while True:
            try:
                user_input = int(input(f"\n[1] Sign-up\n"
                                       f"[2] Enter room\n"
                                       f"[3] Begin consultation\n"
                                       f"[4] Closing time\n"
                                       f"[5] Exit\n"))

            # Input Validation.
                if user_input in (1, 2, 3, 4, 5):
                    break
            except ValueError:
                print("Enter valid input.")

        # Sign up option.
        if user_input == 1:
            name = str(input("Enter your name: "))
            concern = str(input("Enter your concern: "))

            queue.enqueue(name, concern)
            print("Signed-up!")

        # Enter room option.
        elif user_input == 2:
            if queue.is_empty():
                print("No one is in line.")
            else:
                print(queue.enter_room())
        
        # Begin consultation option.
        elif user_input == 3:
            if queue.is_empty():
                print("No one is available.")
            else:
                print(queue.begin_consultation())
        
        # Closing time option.
        elif user_input == 4:
            if queue.is_empty():
                print("No one is in line.")
            else:
                queue.closing_time()
                print("All consultations are done.")
         
        # Exit console loop.
        else:
            print("Console exited.")
            break
