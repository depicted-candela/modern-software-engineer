class TreeNode:
    key: int | str = None
    def __init__(self, key: int | str):
        self.key = key
        self.left_child = None
        self.right_child = None
    def __str__(self):
        return f"key: {self.key}"

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