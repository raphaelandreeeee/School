"""
Arrays in Python
"""


def insert_element(array, element, index=None):
    """
    Inserts an element at the end of the array if no index is provided.
    If an index is provided, the element is inserted at that index.
    """
    if index is not None and index > len(array):
        raise IndexError("Index out of range")

    if index is None:
        array.append(element)
    else:
        array.insert(index, element)


def delete_element(array, index):
    """
    Deletes an element at the given index.
    """
    if index > len(array):
        raise IndexError("Index out of range")

    del array[index]


def reverse_array(array):
    """
    Reverses the array.
    """
    left = 0
    right = len(array) - 1

    if len(array) > 2:
        while left < right:
            # Swapping elements
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1


def main():
    array = [1, 2, 3, 4, 5]

    insert_element(array, 6)
    insert_element(array, 0, 0)
    insert_element(array, 10, 2)
    print(array)                    # Output: [0, 1, 10, 2, 3, 4, 5, 6]

    delete_element(array, 2)
    print(array)                    # Output: [0, 1, 2, 3, 4, 5, 6]

    reverse_array(array)
    print(array)                    # Output: [6, 5, 4, 3, 2, 1, 0]


main()
