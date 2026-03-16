def min_heapify(array, heap_size, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    smallest_index = index

    if (
        left_child_index < heap_size
        and array[left_child_index] < array[smallest_index]
    ):
        smallest_index = left_child_index

    if (
        right_child_index < heap_size
        and array[right_child_index] < array[smallest_index]
    ):
        smallest_index = right_child_index

    if smallest_index != index:
        array[index], array[smallest_index] = array[smallest_index], array[index]
        min_heapify(array, heap_size, smallest_index)


def heap_sort_with_min_heapify(array):
    heap_size = len(array)

    for index in range(heap_size // 2 - 1, -1, -1):
        min_heapify(array, heap_size, index)

    for last_element_index in range(len(array) - 1, 0, -1):
        array[0], array[last_element_index] = array[last_element_index], array[0]
        heap_size -= 1
        min_heapify(array, heap_size, 0)


if __name__ == '__main__':
    nums_list = [21, 38, 29, 17, 4, 25, 32, 9]
    heap_sort_with_min_heapify(nums_list)
    print(nums_list)                            # descending order