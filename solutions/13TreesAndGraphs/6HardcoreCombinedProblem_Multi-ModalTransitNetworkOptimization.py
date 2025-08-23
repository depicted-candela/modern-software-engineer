#       Exercise 5: Hardcore Combined Problem - Multi-Modal Transit 
# Network Optimization
# Objective: Synthesize all concepts from this chunk to build a 
# sophisticated routing algorithm. You will model a complex network, apply 
# different shortest-path algorithms based on different optimization 
# criteria (hops vs. time), and use tree-based logic (LCA) to analyze the 
# resulting paths.

# Problem Description: You are designing an intelligent transit app for a 
# city. The transit system is a mix of fast subways, medium-speed buses, 
# and slow walking paths. It is modeled as a single, large, weighted, 
# directed graph where nodes are locations and edges are transit legs with 
# a travel time weight. A user wants to travel from a start_node to an 
# end_node. Your algorithm must provide two "best" routes:

# The Quickest Route: The path with the minimum possible travel time.
# The Simplest Route: The path with the minimum number of transfers/legs.
# After finding these two distinct optimal paths, your algorithm must 
# identify the Critical Transfer Point: the last common location shared by 
# both paths before they diverge permanently. This point is conceptually 
# the LCA of the two destinations within a combined path structure.
from collections import deque
import heapq

nodes = [
    "Home", "BusStopA", "BusStopB", "Subway1", 
    "Subway2", "Subway3", "Work", "CrossroadX"
]

# (source, dest, time_in_minutes)
edges = [
    ("Home", "BusStopA", 5), 
    ("Home", "CrossroadX", 10), 
    ("CrossroadX", "Subway1", 8), 
    ("BusStopA", "BusStopB", 10), 
    ("BusStopB", "Subway2", 7), 
    ("Subway1", "Subway2", 4), 
    ("Subway2", "Subway3", 4), 
    ("Subway3", "Work", 6), 
    ("BusStopB", "Work", 25) 
    ]

adj_nodes = {node: [] for node in nodes}

for source, destiny, weight in edges:
    adj_nodes[source].append((destiny, weight))

def bfs_path(adjacency_list, start_vertex, end_vertex):
    visited = {start_vertex}
    dequeue = deque([(start_vertex, [start_vertex])])
    while dequeue:
        current_vertex, path = dequeue.popleft()
        if current_vertex == end_vertex: return path
        if current_vertex in adjacency_list:
            for destiny_vertex, _ in adjacency_list[current_vertex]:
                if destiny_vertex not in visited:
                    visited.add(destiny_vertex)
                    dequeue.append((destiny_vertex, path + [destiny_vertex]))
    return None

# distances, histories, first_degree_adjacency

def minimum_dijkstra_path(adjacency_list, start_vertex):
    distances = {vertex: float('infinity') for vertex in adjacency_list}
    prioritized_neighbors = [(0, start_vertex)]
    distances[start_vertex] = 0
    predecessors = {}

    while prioritized_neighbors:
        current_distance, current_vertex = heapq.heappop(prioritized_neighbors)
        if distances[current_vertex] > current_distance: continue
        for next_vertex, next_distance in adjacency_list[current_vertex]:
            distance = current_distance + next_distance
            if distance < distances[next_vertex]:
                predecessors[next_vertex] = current_vertex
                distances[next_vertex] = distance
                heapq.heappush(prioritized_neighbors, (distance, next_vertex))
    return predecessors, distances

def reconstruct_path(predecessors, start, end):
    path = []
    current_node = end
    while current_node != start:
        if current_node not in predecessors: return None
        path.append(current_node)
        current_node = predecessors[current_node]
    path.append(start)
    return path[::-1]

start_node, end_node = "Home", "Work"

predecessors, distances = minimum_dijkstra_path(adj_nodes, start_node)
dijkstra_path = reconstruct_path(predecessors, start_node, end_node)
simplest_path = bfs_path(adj_nodes, start_node, end_node)

def find_lca(minimum_path: list[str], simplest_path: list[str]):
    for path in minimum_path[:-1][::-1]:
        if path in simplest_path[:-1]:
            return path
    return minimum_path[:-1]

print(dijkstra_path)
print(simplest_path)
print(find_lca(dijkstra_path, simplest_path))