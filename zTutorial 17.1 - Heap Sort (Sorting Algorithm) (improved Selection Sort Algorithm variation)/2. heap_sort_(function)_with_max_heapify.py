def max_heapify(array, heap_size, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest_index = index

        # Checking if there is a left child node, and if its larger than the parent node
    if (
        left_child_index < heap_size
        and array[left_child_index] > array[largest_index]
    ):
        largest_index = left_child_index

        # Checking if there is a right child node, and if its larger than the parent node
    if (
        right_child_index < heap_size
        and array[right_child_index] > array[largest_index]
    ):
        largest_index = right_child_index

        # If either of the child nodes is larger than the parent node
    if largest_index != index:
        array[index], array[largest_index] = array[largest_index], array[index]
        max_heapify(array, heap_size, largest_index)


def heap_sort_with_max_heapify(array):
    heap_size = len(array)

    # Build max heap
    for index in range(heap_size // 2 - 1, -1, -1):
        max_heapify(array, heap_size, index)

    # One by one extract an element from max heap
    for last_element_index in range(len(array) - 1, 0, -1):
        # Move current root to end
        array[0], array[last_element_index] = array[last_element_index], array[0]

        # Reduce heap
        heap_size -= 1

        # Call max heapify on the reduced heap
        max_heapify(array, heap_size, 0)


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 32, 9]
    heap_sort_with_max_heapify(nums_list)
    print(nums_list)                            # ascending order