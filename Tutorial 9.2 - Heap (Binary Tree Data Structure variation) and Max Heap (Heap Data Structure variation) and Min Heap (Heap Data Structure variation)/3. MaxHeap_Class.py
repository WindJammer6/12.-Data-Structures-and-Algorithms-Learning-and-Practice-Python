class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child
        self.parent = None  # Parent node

class MaxHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        self.nodes = []   # Full array representation of the heap

    def max_heapify(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest_index = index

        if (
            left_child_index < self.size
            and self.nodes[left_child_index].data > self.nodes[largest_index].data
        ):
            largest_index = left_child_index

        if (
            right_child_index < self.size
            and self.nodes[right_child_index].data > self.nodes[largest_index].data
        ):
            largest_index = right_child_index

        if largest_index != index:
            self.nodes[index].data, self.nodes[largest_index].data = (
                self.nodes[largest_index].data,
                self.nodes[index].data,
            )
            self.max_heapify(largest_index)

    def insert(self, data):
        new_node = HeapNode(data)
        self.nodes.append(new_node)
        self.size += 1

        # First node becomes the root
        if self.size == 1:
            self.root = new_node
            return

        # Connect new node to its parent in the tree
        current_index = self.size - 1
        parent_index = (current_index - 1) // 2
        parent = self.nodes[parent_index]
        new_node.parent = parent

        if parent.left is None:
            parent.left = new_node
        else:
            parent.right = new_node

        # Heapify-up inside insert
        while current_index > 0:
            parent_index = (current_index - 1) // 2

            if self.nodes[current_index].data > self.nodes[parent_index].data:
                self.nodes[current_index].data, self.nodes[parent_index].data = (
                    self.nodes[parent_index].data,
                    self.nodes[current_index].data,
                )
                current_index = parent_index
            else:
                break

    def delete_and_extract_root_node(self):
        if self.size == 0:
            return None

        max_value = self.root.data

        # Case: only one node
        if self.size == 1:
            self.nodes.pop()
            self.root = None
            self.size = 0
            return max_value

        # Remove the last node from the array
        last_node = self.nodes.pop()
        self.size -= 1

        # Disconnect the last node from its parent in the tree
        parent = last_node.parent
        if parent:
            if parent.left is last_node:
                parent.left = None
            elif parent.right is last_node:
                parent.right = None

        # Move last node's value to root
        self.root.data = last_node.data

        # Restore heap property
        self.max_heapify(0)

        return max_value

    def print_heap(self):
        if self.root:
            self._print_heap_recursive(self.root, 0)
        else:
            print("(empty heap)")

    def _print_heap_recursive(self, node, level):
        if node:
            print("   " * level + "|__" + str(node.data))
            if node.left:
                self._print_heap_recursive(node.left, level + 1)
            if node.right:
                self._print_heap_recursive(node.right, level + 1)


def build_max_heap(elements):
    heap = MaxHeap()
    
    for elem in elements:
        heap.insert(elem)
    
    return heap


if __name__ == '__main__':
    numbers = [20, 15, 10, 5, 7, 6, 2, 1]
    numbers_max_heap = build_max_heap(numbers)

    print("Initial heap:")
    numbers_max_heap.print_heap()
    print("Heap array:", [node.data for node in numbers_max_heap.nodes])

    numbers_max_heap.insert(17)
    print("\nAfter inserting 17:")
    numbers_max_heap.print_heap()
    print("Heap array:", [node.data for node in numbers_max_heap.nodes])

    numbers_max_heap.insert(30)
    print("\nAfter inserting 30:")
    numbers_max_heap.print_heap()
    print("Heap array:", [node.data for node in numbers_max_heap.nodes])

    print("\nDelete and extract root node:")
    print(numbers_max_heap.delete_and_extract_root_node())
    numbers_max_heap.print_heap()
    print("Heap array:", [node.data for node in numbers_max_heap.nodes])

    print("\nDelete and extract root node again:")
    print(numbers_max_heap.delete_and_extract_root_node())
    numbers_max_heap.print_heap()
    print("Heap array:", [node.data for node in numbers_max_heap.nodes])