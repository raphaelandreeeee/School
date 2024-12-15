import heaps


class Arrays:
    def __init__(self, size):
        self.size = size
        self.container = []

    def __repr__(self):
        return str(self.container)
    
    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] == self.container[0]
        else:
            return NotImplemented
        
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result
        
    def __gt__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] > self.container[0]
        else:
            return NotImplemented
        
    def __ge__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] >= self.container[0]
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] < self.container[0]
        else:
            return NotImplemented
    
    def __le__(self, other):
        if other.__class__ == self.__class__:
            return other.container[0] <= self.container[0]
        else:
            return NotImplemented

    def insert(self, data, index=None):
        if index is not None and index > len(self.container):
            raise IndexError("Index out of range")

        if index is None:
            self.container.append(data)
        else:
            self.container.insert(index, data)
    
    def delete(self, data, index):
        if index > len(self.container):
            raise IndexError("Index out of range")

        del self.container[index]


class MyHeap(heaps.Heap):
    def __init__(self):
        super().__init__()

    def __getitem__(self, index):
        return self.heap[index]


if __name__ == '__main__':
    container = MyHeap()

    student1 = Arrays(2)
    student2 = Arrays(2)
    student3 = Arrays(2)
    names = (name for name in ["raph", "james", "bill"])

    for student in [student1, student2, student3]:
        student.insert(0)
        student.insert(names.__next__())
        container.insert(student)

    print(container) 
    print(container[0] == container[1])
