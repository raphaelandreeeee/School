class Heap:
    def __init__(self) -> None:
        self.heap = []
        self.size = 0
    
    def __repr__(self) -> str:
        return f"Heap: {self.heap}"

    def _get_parent_index(self, index) -> int:
        return index // 2
    
    def _get_left_child(self, index) -> int:
        return index * 2
    
    def _get_right_child(self, index) -> int:
        return (index * 2) + 1
    
    def _swap(self, index1, index2) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _heapify_up(self, index) -> None:
        parent = self._get_parent_index(index)

        while parent >= 0 and self.heap[parent] < self.heap[index]:
            self._swap(parent, index)
            index = parent
            parent = self._get_parent_index(index)

    def _heapify_down(self, index) -> None:
        left = self._get_left_child(index)
        right = self._get_right_child(index)

        minimum = index

        if left < len(self.heap) and self.heap[left] > self.heap[minimum]:
            self._swap(left, minimum)

        if right < len(self.heap) and self.heap[right] > self.heap[minimum]:
            self._swap(right, minimum)

        if minimum != index:
            self._swap(index, minimum)
            self._heapify_down(minimum)

    def insert(self, data) -> None:
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)
        self.size += 1

    def peek(self) -> int:
        if self.is_empty():
            return None
        
        return self.heap[0]
    
    def delete(self) -> int:
        if self.is_empty():
            return None
        
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self._heapify_down(0)

        return maximum

    def get_maximum(self) -> int:
        return self.heap[0]

    def is_empty(self) -> bool:
        return self.size == 0


if __name__ == '__main__':
    heap = Heap()

    dataset = [10, 20, 50, 30, 40, 90, 100, 70]
    for data in dataset:
        heap.insert(data)

    print(heap)

    print(f"Maximum: {heap.get_maximum()}")
    print(f"Deleted maximum: {heap.delete()}")
    print(heap)
    print(f"Maximum: {heap.get_maximum()}")
