    # Exercise 4: Advanced Tree Logic - Lowest Common Ancestor (LCA)

#   Objective: Implement an algorithm to find the Lowest Common Ancestor (LCA) of two nodes 
# in a binary tree. This problem tests your ability to navigate tree structures and apply 
# recursive logic to solve non-trivial path-based queries.

#   Problem Description: In a file system represented as a directory tree, the LCA of two 
# files/folders represents the smallest directory that contains both of them. This is useful 
# for determining permissions or finding the most specific shared path.

#   Artificial Data: A binary tree structure (note: this is not a BST). Construct this tree 
# manually.

#   Root: _
# Children of /: usr, etc
# Children of usr: local, bin
# Children of local: share, lib
# Children of etc: network, init.d
# Find the LCA of share and lib.
# Find the LCA of lib and init.d.

#       Tasks:

#   Build the Tree: Manually construct the binary tree using the TreeNode class from 
# Exercise 1.

from TreeNode import TreeNode

# Build the binary tree
root = TreeNode("/")
usr = TreeNode("usr")
etc = TreeNode("etc")
root.left_child = usr
root.right_child = etc

local = TreeNode("local")
bin = TreeNode("bin")
usr.left_child = local
usr.right_child = bin

share = TreeNode("share")
lib = TreeNode("lib")
local.left_child = share
local.right_child = lib

network = TreeNode("network")
init = TreeNode("init.d")
etc.left_child = network
etc.right_child = init

#       Implement Recursive LCA: Write a function find_lca(root, node1, node2). The recursive 
# logic is as follows:
#   Base case: If the current node is None or matches one of the target nodes, return the 
# current node.
#   Recursive step: Search for the nodes in the left and right subtrees.
#   Logic:
# If the recursive calls on both left and right subtrees return a non-null node, then the 
# current node is the LCA.
# Otherwise, if only one of them returns a non-null node, that returned node is the LCA (or 
# contains the LCA).

def find_lca(root: TreeNode, left_child, right_child):
    if root == None or root.key in {left_child, right_child}:
        return root
    left = find_lca(root.left_child, left_child, right_child)
    right = find_lca(root.right_child, left_child, right_child)
    if left and right: return root
    return left if left else right

print(find_lca(root, "share", "lib"))
print(find_lca(root, "usr", "etc"))
