#   Exercise 3: Weighted Shortest Path with Dijkstra's Algorithm

# Objective: Solve a single-source shortest path problem on a weighted 
# graph using Dijkstra's algorithm. This exercise introduces the concept of 
# path cost (not just hops) and requires using a priority queue for an 
# efficient implementation.

# Problem Description: A logistics company needs to find the fastest 
# delivery routes from its main warehouse ('A') to all other distribution 
# centers. The network is represented as a weighted directed graph where 
# edge weights are the travel times in hours.

#   Artificial Data:
# A set of distribution centers: 
nodes = ["A", "B", "C", "D", "E", "F"]
# A list of one-way routes with travel times: 
routes = [
    ("A", "B", 7), 
    ("A", "C", 9), 
    ("A", "F", 14), 
    ("B", "C", 10), 
    ("B", "D", 15), 
    ("C", "D", 11), 
    ("C", "F", 2), 
    ("D", "E", 6), 
    ("E", "F", 9)
]

#   Tasks:
# Represent the Weighted Graph: Use an adjacency list (a dictionary) where 
# keys are source nodes and values are lists of tuples, with each tuple 
# containing (destination_node, weight).
adjacent_graph = {node: [] for node in nodes}
for source, destiny, weight in routes:
    adjacent_graph[source].append((destiny, weight))

# Implement Dijkstra's Algorithm: Write a function 
# dijkstra(graph, start_node) that computes the shortest travel time from 
# start_node to every other node.

# Use a priority queue to efficiently retrieve the unvisited node with the 
# smallest distance. Python's heapq module is perfect for this.
# Store the minimum distances in a dictionary or array.
# Store the predecessors (parents) to allow for path reconstruction.
# Output the Results: The function should return two dictionaries: one 
# mapping each node to its shortest distance from the start, and another 
# mapping each node to its predecessor in the shortest path.

import heapq

def dijkstra(graph, start_node):
    predecessors = {}
    prioritized_neighbors = [(0, start_node)]
    distances = {node: float("infinity") for node in graph}
    distances[start_node] = 0

    while prioritized_neighbors:
        current_distance, current_node = heapq.heappop(prioritized_neighbors)
        if distances[current_node] > current_distance: continue
        for next_node, next_distance in graph[current_node]:
            distance = next_distance + current_distance
            if distance < distances[next_node]:
                distances[next_node] = distance
                predecessors[next_node] = current_node
                heapq.heappush(prioritized_neighbors, (distance, next_node))
    return distances, predecessors

def reconstruct_path(predecessors, start, end):
    path = []
    current_node = end
    while current_node != start:
        if current_node not in predecessors: return None
        path.append(current_node)
        current_node = predecessors[current_node]
    path.append(start)
    return path[::-1]

start, end = 'A', 'F'
distances, predecessors = dijkstra(adjacent_graph, start)

print(reconstruct_path(predecessors, start, end))