import json

# Artificial Data: A small project dependency graph
tasks = ["Compile", "Test", "Lint", "Deploy", "Document", "Release"]
dependencies = [
    ("Compile", "Test"), 
    ("Compile", "Lint"), 
    ("Test", "Deploy"), 
    ("Lint", "Deploy"), 
    ("Deploy", "Document"), 
    ("Document", "Release")
]

# Build adjacency list for a directed graph
adj_list = {task: [] for task in tasks}
for prereq, task in dependencies:
    adj_list[prereq].append(task)

# print("Adjacency List for Task Dependencies:")
# print(json.dumps(adj_list, indent=2))


# from collections import deque

# def bfs_shortest_path(graph, start_node, end_node):
#     queue = deque([(start_node, [start_node])])
#     visited = {start_node}
#     while queue:
#         current_node, path = queue.popleft()
#         if current_node == end_node:
#             return path
#         # Ensure current_node is a valid key before accessing it
#         if current_node in graph:
#             for neighbor in graph[current_node]:
#                 if neighbor not in visited:
#                     visited.add(neighbor)
#                     queue.append((neighbor, path + [neighbor]))
#     return None

# # --- Example Usage ---
# path = bfs_shortest_path(adj_list, "Compile", "Release")
# print(f"\nMinimum dependency chain from Compile to Release: {path}")


import heapq

def dijkstra_shortest_path(graph, start_node):
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessors = {}

    while priority_queue:
        print(f"Queue {priority_queue}")
        current_dist, current_node = heapq.heappop(priority_queue)
        if current_dist > distances[current_node]: continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, predecessors

def reconstruct_path(predecessors, start, end):
    path = []
    current = end
    while current != start:
        if current not in predecessors: return None
        path.append(current)
        current = predecessors[current]
    path.append(start)
    return path[::-1]

# --- Example Usage ---
# Artificial Data: A network of servers with latency in ms
network = {
    'A': {'B': 5, 'C': 2}, 'B': {'D': 4, 'E': 2},
    'C': {'B': 8, 'E': 7}, 'D': {'E': 6, 'F': 3},
    'E': {'F': 1}, 'F': {}
}
# Add all nodes to the graph for completeness
all_nodes = set(network.keys())
for node, edges in network.items():
    all_nodes.update(edges.keys())
for node in all_nodes:
    if node not in network:
        network[node] = {}

print(f"Network: {network}")

start, end = 'A', 'F'
distances, predecessors = dijkstra_shortest_path(network, start)

print(f"Distances {distances}")
print(f"Predecessors {predecessors}")

path = reconstruct_path(predecessors, start, end)

print("\n--- Dijkstra's Algorithm ---")
print(f"Lowest latency from {start} to {end}: {distances.get(end, 'N/A')}ms")
print(f"Path: {path}")