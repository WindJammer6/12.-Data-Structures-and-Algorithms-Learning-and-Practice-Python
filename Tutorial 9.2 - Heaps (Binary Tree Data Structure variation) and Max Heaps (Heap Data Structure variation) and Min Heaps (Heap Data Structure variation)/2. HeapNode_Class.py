# Exactly the same as the 'BinarySearchTreeNode' class in the '2. BinarySearchTreeNode_Class.py' file in the
# 'Tutorial 9.1 - Binary Trees (Tree Data Structure variation) and Binary Search Trees (Binary Tree Data Structure 
# variation)' folder
class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Left child
        self.right = None  # Right child
        self.parent = None  # Parent node