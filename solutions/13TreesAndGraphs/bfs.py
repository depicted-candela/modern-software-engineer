import json

# Artificial Data: A small project dependency graph
tasks = ["Compile", "Test", "Lint", "Deploy", "Document", "Release"]
dependencies = [("Compile", "Test"), ("Compile", "Lint"), ("Test", "Deploy"), ("Lint", "Deploy"), ("Deploy", "Document"), ("Document", "Release")]

# Build adjacency list for a directed graph
adj_list = {task: [] for task in tasks}
for prereq, task in dependencies:
    adj_list[prereq].append(task)

print("Adjacency List for Task Dependencies:")
print(json.dumps(adj_list, indent=2))


from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
    queue = deque([(start_node, [start_node])])
    visited = {start_node}
    while queue:
        current_node, path = queue.popleft()
        print(f"CURRENT NODE: {current_node}")
        print(f"PATH: {path}")
        if current_node == end_node:
            return path
        # Ensure current_node is a valid key before accessing it
        if current_node in graph:
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    return None

# --- Example Usage ---
path = bfs_shortest_path(adj_list, "Compile", "Release")
print(f"\nMinimum dependency chain from Compile to Release: {path}")