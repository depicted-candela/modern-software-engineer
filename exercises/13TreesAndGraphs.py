employee_ids = [50, 30, 70, 20, 40, 60, 80, 25, 35, 75]

class TreeNode:
    """A node in our digital family tree."""
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    """The library's filing system for our data."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        # Decide which branch to go down
        if key < current_node.key:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(key)
            else:
                self._insert_recursive(current_node.left_child, key)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(key)
            else:
                self._insert_recursive(current_node.right_child, key)

    def inorder_traversal(self):
        """Returns a list of keys from an inorder traversal."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left_child, result)
            result.append(node.key)
            self._inorder_recursive(node.right_child, result)

    def preorder_traversal(self):
        """Returns a list of keys from a preorder traversal."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left_child, result)
            self._preorder_recursive(node.right_child, result)

    def postorder_traversal(self):
        """Returns a list of keys from a postorder traversal."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left_child, result)
            self._postorder_recursive(node.right_child, result)
            result.append(node.key)

# Example Usage
bst = BinarySearchTree()
for emp_id in employee_ids:
    bst.insert(emp_id)

print(f"Inorder (Sorted): {bst.inorder_traversal()}")
print(f"Preorder: {bst.preorder_traversal()}")
print(f"Postorder: {bst.postorder_traversal()}")