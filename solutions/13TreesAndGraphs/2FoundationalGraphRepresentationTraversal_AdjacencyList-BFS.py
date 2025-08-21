#   Exercise 2: Foundational Graph Representation & Traversal (Adjacency List & BFS)

# Objective: Represent a graph using an adjacency list and implement Breadth-First Search 
# (BFS) to find the shortest path between two nodes in terms of the number of connections. 
# This exercise establishes your ability to model networked data and apply queue-based 
# traversal algorithms.

#   Problem Description: You need to model a small social network to find the "degree of 
# separation" between two individuals. The degree of separation is the smallest number of 
# friendship links required to connect two people.

#   Artificial Data:

# A set of users: 
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
# A list of friendships (undirected edges): 
friendships = [
  ("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), 
  ("Charlie", "Eve"), ("David", "Eve"), ("Eve", "Frank"), ("David", "Grace")
]

friends_adjlist = {user: [] for user in users}
for user, friend in friendships:
  friends_adjlist[user].append(friend)
# Find the shortest path from "Alice" to "Frank" and from "Bob" to "Grace".

#   Tasks:

# Represent the Graph: Create a graph representation using a Python dictionary, where each key 
# is a user and the corresponding value is a list of their friends. This is the adjacency list 
# pattern and leverages Python Dictionaries from Chunk 1. Remember that friendships are mutual 
# (undirected edges).

#   Implement BFS: 
# Write a function bfs_shortest_path(graph, start_node, end_node) that performs 
# a BFS traversal to find the shortest path.
# Use a queue (collections.deque is ideal, building on Chunk 12) to keep track of nodes to 
# visit.

# Keep track of visited nodes to avoid cycles and redundant processing.
# Store the path by tracking the parent of each node as you visit it.
# Reconstruct and Return Path: Once the end_node is reached, reconstruct the path from 
# end_node back to start_node using the parent pointers. Return the path as a list of user 
# names.
from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
  visited = {start_node}
  queue = deque([(start_node, [start_node])])
  while queue:
    curent_node, path = queue.popleft()
    if curent_node == end_node: return path
    if curent_node in graph:
      for friend in graph[curent_node]:
        if friend not in visited:
          visited.add(friend)
          queue.append((friend, path + [friend]))
print(bfs_shortest_path(friends_adjlist, 'Alice', 'Frank'))
print(bfs_shortest_path(friends_adjlist, 'Bob', 'Grace'))