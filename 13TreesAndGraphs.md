<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture: A Unified Theory of Trees and Graphs</title>
    <link rel="stylesheet" href="styles/lecture.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code&family=Lato:wght@400;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>

<div class="toc-popup-container">
    <input type="checkbox" id="toc-toggle" class="toc-toggle-checkbox">
    <label for="toc-toggle" class="toc-toggle-label">
        <span>Lecture Navigation</span>
        <span class="toc-icon-open"></span>
    </label>
    <div class="toc-content">
        <h4>Table of Contents</h4>
        <ul>
            <li><a href="#part1-trees">Part 1: Trees - The Disciplined Hierarchy</a>
                <ul>
                    <li><a href="#section1-1">1.1 Core Concepts</a></li>
                    <li><a href="#section1-2">1.2 Binary Search Tree (BST)</a></li>
                </ul>
            </li>
            <li><a href="#part2-traversal">Part 2: Traversing Trees with DFS</a>
                <ul>
                    <li><a href="#section2-1">2.1 Inorder Traversal</a></li>
                    <li><a href="#section2-2">2.2 Preorder Traversal</a></li>
                    <li><a href="#section2-3">2.3 Postorder Traversal</a></li>
                </ul>
            </li>
            <li><a href="#part3-graphs">Part 3: Graphs - The Networked Reality</a>
                <ul>
                    <li><a href="#section3-1">3.1 Graph Concepts</a></li>
                    <li><a href="#section3-2">3.2 Adjacency List</a></li>
                    <li><a href="#section3-3">3.3 Breadth-First Search (BFS)</a></li>
                </ul>
            </li>
            <li><a href="#part4-dijkstra">Part 4: Dijkstra's Algorithm</a>
                <ul>
                    <li><a href="#section4-1">4.1 Weighted Graphs</a></li>
                    <li><a href="#section4-2">4.2 Dijkstra's Shortest Path</a></li>
                </ul>
            </li>
            <li><a href="#part5-hardcore">Part 5: Hardcore Problem & Immersion Joke</a></li>
        </ul>
    </div>
</div>

<div class="container">
    <h1>A Unified Theory of Trees and Graphs</h1>

<h2 id="part1-trees">Part 1: Trees - The Disciplined Hierarchy</h2>

<h3 id="section1-1">1.1 Core Concepts: The Thought Architecture of Trees</h3>

<blockquote class="rhyme">
    Why did the binary search tree break up with the AVL tree? It said, "You're just too balanced for me! I need some spontaneity."
</blockquote>

<p>
    A <strong>tree</strong> is a connected graph with no cycles. It is the foundational model for any pure hierarchy. Think of it as a <em>thought architecture</em>:
</p>
<ul>
    <li><strong>Root</strong>: The <em>single ancestor</em>, the origin point of the entire structure.</li>
    <li><strong>Nodes</strong>: The individual concepts or data points.</li>
    <li><strong>Edges</strong>: The <em>hereditary links</em> connecting a parent to a child.</li>
    <li><strong>Leaves</strong>: <em>Terminal thoughts</em>—nodes at the end of a branch with no children.</li>
</ul>

<div class="caution">
    <h4>The Rules of the Hierarchy (Properties)</h4>
    <ul>
        <li>A tree with <em>N</em> nodes is held together by a surprisingly fragile skeleton of exactly <em>N-1</em> edges.</li>
        <li>This structure is a <strong>veil of simplicity</strong>: it guarantees a unique path between any two nodes. No confusing detours.</li>
        <li>Adding one more edge creates a cycle—an <em>unwanted conversation loop</em>.</li>
        <li>Removing any single edge causes a schism, splitting the tree into two. Every connection is critical.</li>
    </ul>
</div>

<p><small><strong>Source & Theory</strong>: <code>DiscreteMathematicsandItsApplications_KennethHRosen_2018/18_Chapter_11_Trees.pdf</code>, Section 11.1. These properties define the fundamental nature of trees as minimally connected graphs.</small></p>

<h3 id="section1-2">1.2 Concept: The Binary Search Tree (BST) - A Disciplined Cascade</h3>

<p>
    A Binary Search Tree is a binary tree that enforces a strict, almost magical, ordering on its data. It's a <strong>disciplined cascade</strong> where data finds its own sorted place.
</p>
<div class="oracle-specific">
    <h4>The BST Property</h4>
    For any given node <code>n</code> with key <code>k</code>:
    <ol>
        <li>Its left subtree is its <strong>past</strong>: every key there is <em>less than</em> <code>k</code>.</li>
        <li>Its right subtree is its <strong>future</strong>: every key there is <em>greater than or equal to</em> <code>k</code>.</li>
    </ol>
    This property is the key to achieving <strong>instantaneous memory</strong>. It transforms a linear O(n) search into a logarithmic O(log n) dive, making it the backbone for fast lookups in databases and symbol tables.
</div>

<blockquote class="rhyme">
    A binary search tree walks into a bar. It goes to the left side, then the right, then left again. The bartender asks, "What are you looking for?" The tree says, "My key!"
</blockquote>
    
```python
# An object representing a single, potentially lonely, thought in our architecture.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left_child = None  # The past, forever in the shadow of the present.
        self.right_child = None # The future, always greater.

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    # A recursive plunge into the tree's depths.
    def _insert_recursive(self, current_node, key):
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

# --- Example Usage ---
# Artificial Data: Priority levels for system alerts
alert_priorities = [50, 30, 70, 20, 40, 60, 80]
bst = BinarySearchTree()
for priority in alert_priorities:
    bst.insert(priority)

print("BST constructed successfully. The hierarchy is established.")
```
<p><small><strong>Source & Theory</strong>: <code>IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/Chapter_12_Binary_Search_Trees.pdf</code>, Sections 12.1 & 12.3. The code is a direct implementation of the recursive insertion logic that maintains the BST's core invariant.</small></p>

<h2 id="part2-traversal">Part 2: Traversing Trees with DFS</h2>

<p>DFS traversals are different ways to perform a <strong>plunging descent</strong> through the tree, visiting every node.</p>

<h3 id="section2-1">2.1 Inorder Traversal: The Historian's Path (Left, Root, Right)</h3>
<ul>
    <li><strong>Property (Grounded)</strong>: This is a <em>sorted pilgrimage</em>. In a BST, it visits nodes in ascending key order.</li>
    <li><strong>Utility Context</strong>: The canonical way to extract sorted data from a BST.</li>
</ul>

<h3 id="section2-2">2.2 Preorder Traversal: The CEO's Decree (Root, Left, Right)</h3>
<ul>
    <li><strong>Property (Grounded)</strong>: A <em>commanding presence</em>. The root (the boss) is processed first, before delegating to its sub-hierarchies.</li>
    <li><strong>Utility Context</strong>: Perfect for creating an exact, reconstructible copy of the tree.</li>
</ul>

<h3 id="section2-3">2.3 Postorder Traversal: The Engineer's Teardown (Left, Right, Root)</h3>
<ul>
    <li><strong>Property (Grounded)</strong>: A <em>foundational summary</em>. You process all children before their parent.</li>
    <li><strong>Utility Context</strong>: The only safe way to delete all nodes in a tree, ensuring you don't delete a parent before its children.</li>
</ul>
    
```python
# Continuing the BinarySearchTree class...
class BinarySearchTree:
    # --- existing __init__ and insert methods ---
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, current_node, key):
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
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left_child, result)
            result.append(node.key)
            self._inorder_recursive(node.right_child, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.key)
            self._preorder_recursive(node.left_child, result)
            self._preorder_recursive(node.right_child, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left_child, result)
            self._postorder_recursive(node.right_child, result)
            result.append(node.key)

# --- Example Usage ---
bst = BinarySearchTree()
alert_priorities = [50, 30, 70, 20, 40, 60, 80]
for priority in alert_priorities:
    bst.insert(priority)

print(f"Inorder (Historian): {bst.inorder_traversal()}")
print(f"Preorder (CEO): {bst.preorder_traversal()}")
print(f"Postorder (Engineer): {bst.postorder_traversal()}")
```
<p><small><strong>Source & Theory</strong>: <code>DiscreteMathematicsandItsApplications_KennethHRosen_2018/18_Chapter_11_Trees.pdf</code>, Section 11.3. The three recursive patterns directly map to the formal definitions of these traversals.</small></p>

<h2 id="part3-graphs">Part 3: Graphs - The Networked Reality</h2>

<h3 id="section3-1">3.1 Graph Concepts & Representation: The Digital Address Book</h3>
<p>
    A graph models a <strong>networked reality</strong> where connections are not necessarily hierarchical. Unlike a tree, a graph can be a tangled web of relationships. An <strong>adjacency list</strong> is its most common representation—a <em>digital address book</em> where each vertex has a list of its direct connections.
</p>
<div class="postgresql-bridge">
    <h4>Advantage: Lean Infrastructure</h4>
    <p>For a social network, you only store actual friendships, not the infinite list of non-friendships. This makes it incredibly space-efficient for sparse graphs, which most real-world networks are. This is a crucial principle for <strong>Scalability</strong>.</p>
</div>

```python
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
```
<p><small><strong>Source & Theory</strong>: <code>IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/20_Chapter_20_Elementary_Graph_Algorithms.pdf</code>, Section 20.1.</small></p>

<h3 id="section3-3">3.2 Algorithm: BFS - Ripples in a Pond</h3>
<p>
    BFS is a <strong>patient exploration</strong>. It doesn't dive deep; it expands its search in concentric circles, like <em>ripples in a pond</em>. It relies on a <strong>queue (FIFO)</strong> to manage this layer-by-layer exploration.
</p>
<div class="oracle-specific">
    <h4>Property: The Shockwave of Discovery</h4>
    For unweighted graphs, this ripple effect guarantees that the first time BFS reaches a node, it has done so via the absolute shortest path in terms of edge count.
</div>

```python
from collections import deque

def bfs_shortest_path(graph, start_node, end_node):
    queue = deque([(start_node, [start_node])])
    visited = {start_node}
    while queue:
        current_node, path = queue.popleft()
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
```
<p><small><strong>Source & Theory</strong>: <code>IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/20_Chapter_20...</code>, Section 20.2.</small></p>

<h2 id="part4-dijkstra">Part 4: Dijkstra's Algorithm - The Greedy Conquest</h2>
<blockquote class="rhyme">
    "Don't worry if Dijkstra's algorithm seems intimidating. The first time I tried to implement it, my code just kept finding the shortest path to the coffee machine. We'll get there."
</blockquote>
<p>
    Dijkstra's algorithm finds the shortest path in a <strong>weighted</strong> graph, turning a simple map into a <em>logistical landscape</em>. It is a <strong>greedy conquest</strong>, a <em>dancing volcano</em> of updates. At every step, it makes the locally optimal choice: it explores from the unvisited node currently closest to the start.
</p>
<p>This greedy choice is made efficient by a <strong>min-priority queue</strong> (<code>heapq</code>), which acts as the algorithm's <em>council of advisors</em>, always suggesting the most promising next step.</p>
<div class="caution">
    <h4>Limitation: A Brittle Solution</h4>
    <p>Its greedy nature is also its weakness. It fails spectacularly with negative edge weights, creating a <em>spinning void</em> of incorrect assumptions because it cannot revise a path choice once a node has been finalized.</p>
</div>

```python
import heapq

def dijkstra_shortest_path(graph, start_node):
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]
    predecessors = {}

    while priority_queue:
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

start, end = 'A', 'F'
distances, predecessors = dijkstra_shortest_path(network, start)
path = reconstruct_path(predecessors, start, end)

print("\n--- Dijkstra's Algorithm ---")
print(f"Lowest latency from {start} to {end}: {distances.get(end, 'N/A')}ms")
print(f"Path: {path}")
```
<p><small><strong>Source & Theory</strong>: <code>IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/22_Chapter_22_Single-Source_Shortest_Paths.pdf</code>, Section 22.3.</small></p>

<h2 id="part5-hardcore">Part 5: Hardcore Problem & Immersion Joke - The Ministry of Procedural Efficiency</h2>
<div class="oracle-specific">
    <h4>Immersion Joke: The Capstone Example</h4>
    <p>Today, we are architecting the "Inter-Departmental Memo Delivery System" for the Ministry of Procedural Efficiency. Our client needs to send a critical memo from the <code>Sub-Basement Archives</code> to the <code>Office of the Chief Visionary Officer</code>.</p>
    <p>We must provide two routes:</p>
    <ol>
        <li><strong>The Intern's Route (Simplest)</strong>: The path with the fewest transit legs—a <em>foolproof corridor</em>.</li>
        <li><strong>The CEO's Route (Quickest)</strong>: The path with minimum travel time—the <em>executive express</em>.</li>
    </ol>
    <p>Finally, we must identify the <strong>Decision Nexus</strong>: the last shared location before these two optimal paths diverge.</p>
</div>
    
```python
# Artificial Data: Ministry Network
ministry_network = {
    'Sub-Basement Archives': {'Pneumatic Hub A': 10, 'Dumbwaiter Central': 15},
    'Pneumatic Hub A': {'Pneumatic Hub B': 5, 'Quantum Tunnel Input': 20},
    'Dumbwaiter Central': {'Pneumatic Hub B': 8},
    'Pneumatic Hub B': {'Office of Redundancy Office': 10, 'Quantum Tunnel Input': 1},
    'Quantum Tunnel Input': {'Quantum Tunnel Output': 0.1},
    'Quantum Tunnel Output': {"Chief Visionary's Antechamber": 0.1},
    'Office of Redundancy Office': {"Chief Visionary's Antechamber": 12},
    "Chief Visionary's Antechamber": {"Office of the Chief Visionary Officer": 1},
    "Office of the Chief Visionary Officer": {} # Ensure end node is in graph
}
start_dept = 'Sub-Basement Archives'
end_dept = 'Office of the Chief Visionary Officer'

# 1. Build unweighted graph for BFS
unweighted_ministry = {dept: list(connections.keys()) for dept, connections in ministry_network.items()}

# 2. Find Intern's Route (BFS)
intern_path = bfs_shortest_path(unweighted_ministry, start_dept, end_dept)
print(f"\nIntern's Route (Simplest): {intern_path}")

# 3. Find CEO's Route (Dijkstra)
distances, predecessors = dijkstra_shortest_path(ministry_network, start_dept)
ceo_path = reconstruct_path(predecessors, start_dept, end_dept)
print(f"CEO's Route (Quickest): {ceo_path} in {distances[end_dept]} minutes")

# 4. Find Decision Nexus (LCA Logic)
intern_set = set(intern_path)
decision_nexus = None
# Trace CEO's path backwards to find the last common node
if ceo_path:
    for node in reversed(ceo_path):
        if node in intern_set:
            decision_nexus = node
            break
print(f"The Decision Nexus is: '{decision_nexus}'")
```
<p><small><strong>Source & Theory</strong>: This problem is a synthesis. It uses the <strong>Adjacency List</strong> pattern (Cormen 20.1), <strong>BFS</strong> (Cormen 20.2), <strong>Dijkstra's Algorithm</strong> (Cormen 22.3), and applies tree-based <strong>LCA logic</strong> to the resulting path structures derived from predecessor subgraphs (Rosen 11.1). The humor transforms it into a memorable <strong>Fictional Case Study</strong>.</small></p>
</div>

</body>