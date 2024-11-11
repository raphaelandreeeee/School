class Notebooks:
    """
    Uses stack implementation
    """
    
    def __init__(self) -> None:
        self.stack = []
        self.size = 0
    
    def add_notebook(self, name) -> None:
        """
        Appends the notebook on top of the stack.
        """
        
        self.stack += [name]
        self.size += 1

    def check_notebook(self) -> str:
        """
        Pops the notebook on top of the stack.
        """
        
        item = self.stack[-1]
        del self.stack[-1]
        self.size -= 1

        return item
    
    def peek_notebook(self) -> str:
        """
        Peeks at the notebook on top of the stack.
        """
        
        return self.stack[-1]
    
    def check_all(self) -> list:
        """
        Returns and deletes the whole stack of notebooks.
        """
        
        notebooks = self.stack
        self.stack = []
        self.size = 0

        return notebooks
    
    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty. Returns False, otherwise.
        """
        
        return self.size == 0
    

if __name__ == '__main__':
    notebooks = Notebooks()

    # Console loop.
    while True:
        # User input loop.
        while True:
            try:
                user_input = int(input(f"[1] Add Notebook\n"
                                       f"[2] Check Notebook\n"
                                       f"[3] Peek Notebook\n"
                                       f"[4] Check all\n"
                                       f"[5] Exit\n"))
                
            # Input Validation. 
                if user_input in (1, 2, 3, 4, 5):
                    break
            except ValueError:
                print("Enter valid input.")

        # Add notebook option.
        if user_input == 1:
            name = str(input("Enter name for notebook: ")) 
            notebooks.add_notebook(name)

            print(f"\nNotebook Added!\n")

        # Check notebook option.
        elif user_input == 2:
            if notebooks.is_empty():
                print("No notebooks to check.")
            else:
                notebook = notebooks.check_notebook()

                print(f"\n{notebook}'s notebook is being checked.")

        # Peek notebook option.
        elif user_input == 3:
            if notebooks.is_empty():
                print("No notebooks available.")
            else:
                notebook = notebooks.peek_notebook()

                print(f"{notebook}'s is at the top.")
        
        # Check all notebooks option.
        elif user_input == 4:
            if notebooks.is_empty():
                print("No notebooks to check.")
            else:
                stack = notebooks.check_all()

                for notebook in reversed(stack):
                    print(f"{notebook}'s is being checked.")

        # Exit console loop.
        else:
            print("Console Exited.")
            break
    