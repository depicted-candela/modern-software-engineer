#   Exercise 1: Foundational Tree Representation & Traversal (BST & DFS)
# Objective: Implement a Binary Search Tree (BST) data structure from scratch. You 
# will implement node insertion that respects the BST property and then perform 
# Depth-First Search (DFS) traversals (inorder, preorder, postorder) to verify its 
# structure and properties. This exercise solidifies your understanding of tree 
# nodes, hierarchical data, and the fundamental pattern of recursive tree processing.

# Problem Description: A company is organizing its employee database. To enable 
# efficient lookups, they decide to store employee records in a Binary Search Tree, 
# using a unique integer employee ID as the key. Your task is to build this BST and 
# implement the standard traversals to list the employees in different orders.
employee_ids = [50, 30, 70, 20, 40, 60, 80, 25, 35, 75]

class TreeNode:
    key: int | str = None
    def __init__(self, key: int | str):
        self.key = key
        left_child = None
        right_child = None

class BinarySearchTree:
    root: TreeNode = None
    
    def insert(self, key):
        if self.root is None: self.root = TreeNode(key)
        else: self.insert_recursive(self.root, key)
    
    def insert_recursive(self, current_node: TreeNode, new_key: int):
        if current_node.key > new_key:
            if current_node.left_child is None: 
                current_node.left_child = TreeNode(new_key)
            else:
                self.insert_recursive(current_node.left_child, new_key)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(new_key)
            else: self.insert_recursive(current_node.right_child, new_key)

    def inorder_traversal(self):
        buffer = []
        self.recursive_inorder_traversal(self.root, buffer)
        return buffer

    def recursive_inorder_traversal(self, node: TreeNode, buffer: list[int]):
        if node:
            self.recursive_inorder_traversal(node.left_child, buffer)
            buffer.append(node.key)
            self.recursive_inorder_traversal(node.right_child, buffer)
    
    def preorder_traversal(self):
        buffer = []
        self.recursive_preorder_traversal(self.root, buffer)
        return buffer

    def recursive_preorder_traversal(self, node: TreeNode, buffer: list[int]):
        if node:
            buffer.append(node.key)
            self.recursive_preorder_traversal(node.left_child, buffer)
            self.recursive_preorder_traversal(node.right_child, buffer)
    
    def postorder_traversal(self):
        buffer = []
        self.recursive_postorder_traversal(self.root, buffer)
        return buffer
    
    def recursive_postorder_traversal(self, node: TreeNode, buffer: list[int]):
        if node:
            self.recursive_postorder_traversal(node.left_child, buffer)
            self.recursive_postorder_traversal(node.right_child, buffer)
            buffer.append(node.key)
    
bfs = BinarySearchTree()
for employee in employee_ids:
    bfs.insert(employee)
print(f"Normal traversal:    {employee_ids}")
print(f"Inorder traversal:   {bfs.inorder_traversal()}")
print(f"Preorder traversal:  {bfs.preorder_traversal()}")
print(f"Postorder traversal: {bfs.postorder_traversal()}")