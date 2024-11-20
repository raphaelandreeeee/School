import math

class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    def __repr__(self) -> str:
        return "".join(str(item) for item in self.hash_table)

    def _hash_function(self, key) -> int:
        A = (math.sqrt(5) - 1) / 2

        return math.floor(self.size * ((key * A) % 1))

    def insert(self, key, value) -> None:
        hashed_key = self._hash_function(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key) -> None:
        hashed_key = self._hash_function(key) % self.size
        
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "No record found"

    def delete(self, key) -> None:
        hashed_key = self._hash_function(key) % self.size
        
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return


if __name__ == '__main__':
    hashtable = HashTable(4)

    dataset = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
    for key, value in dataset.items():
        hashtable.insert(key, value)

    print(hashtable)

    hashtable.delete(1)

    print(hashtable)

    print(hashtable.search(2))
