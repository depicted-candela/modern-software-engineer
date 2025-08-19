# Exercise 1: Foundational Tree Representation & Traversal (BST & DFS)

**Objective**: Implement a Binary Search Tree (BST) data structure from scratch. You will implement node insertion that respects the BST property and then perform Depth-First Search (DFS) traversals (inorder, preorder, postorder) to verify its structure and properties. This exercise solidifies your understanding of tree nodes, hierarchical data, and the fundamental pattern of recursive tree processing.

**Problem Description**: A company is organizing its employee database. To enable efficient lookups, they decide to store employee records in a Binary Search Tree, using a unique integer employee ID as the key. Your task is to build this BST and implement the standard traversals to list the employees in different orders.

**Artificial Data**:
A list of employee IDs to be inserted into the BST:
`employee_ids = [50, 30, 70, 20, 40, 60, 80, 25, 35, 75]`

**Tasks**:
1.  **Define the `TreeNode` Class**: Create a Python class `TreeNode` with attributes `key`, `left_child`, and `right_child`. This leverages **OOP concepts from Chunk 5**.
2.  **Define the `BinarySearchTree` Class**: Create a class `BinarySearchTree` with an attribute `root`.
3.  **Implement `insert` Method**: Inside `BinarySearchTree`, create a recursive method `insert(key)` that adds a new node while maintaining the BST property: for any node `n`, all keys in `n`'s left subtree are less than `n.key`, and all keys in its right subtree are greater than `n.key`.
4.  **Implement DFS Traversals**: Implement three recursive methods:
    *   `inorder_traversal()`: Should visit nodes in ascending order of keys (Left, Root, Right).
    *   `preorder_traversal()`: Should visit the root before its children (Root, Left, Right).
    *   `postorder_traversal()`: Should visit the root after its children (Left, Right, Root).
5.  **Verification**: Create an instance of the `BinarySearchTree`, insert all the `employee_ids`, and print the result of each traversal. The inorder traversal should output a sorted list.

**Relevant Sources & Theory**:
*   **Source**: `IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/Chapter_12_Binary_Search_Trees.pdf`
    *   **Theory**: Sections 12.1 ("What is a binary search tree?") and 12.3 ("Insertion and deletion") provide the formal definition of the binary-search-tree property and the logic for insertion. The `INORDER-TREE-WALK` pseudocode is the basis for your traversal methods.
*   **Source**: `DiscreteMathematicsandItsApplications_KennethHRosen_2018/18_Chapter_11_Trees.pdf`
    *   **Theory**: Section 11.3 ("Tree Traversal") formally defines preorder, inorder, and postorder traversals, which directly map to the methods you need to implement. This provides the mathematical foundation for why these traversal orders are distinct and useful.

**Software Engineering Principles**:
*   **Modifiability**: Your BST class should be designed so that new operations (e.g., `delete`, `search`) can be added easily without changing existing traversal or insertion logic.
*   **Testability**: The deterministic output of traversals (especially `inorder`) makes the data structure easy to test. A correct `inorder_traversal` that produces a sorted list is a strong indicator of a correct `insert` method.

---

# Exercise 2: Foundational Graph Representation & Traversal (Adjacency List & BFS)

**Objective**: Represent a graph using an adjacency list and implement Breadth-First Search (BFS) to find the shortest path between two nodes in terms of the number of connections. This exercise establishes your ability to model networked data and apply queue-based traversal algorithms.

**Problem Description**: You need to model a small social network to find the "degree of separation" between two individuals. The degree of separation is the smallest number of friendship links required to connect two people.

**Artificial Data**:
*   A set of users: `users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]`
*   A list of friendships (undirected edges): `friendships = [("Alice", "Bob"), ("Alice", "Charlie"), ("Bob", "David"), ("Charlie", "Eve"), ("David", "Eve"), ("Eve", "Frank"), ("David", "Grace")]`
*   Find the shortest path from "Alice" to "Frank" and from "Bob" to "Grace".

**Tasks**:
1.  **Represent the Graph**: Create a graph representation using a Python dictionary, where each key is a user and the corresponding value is a list of their friends. This is the **adjacency list pattern** and leverages **Python Dictionaries from Chunk 1**. Remember that friendships are mutual (undirected edges).
2.  **Implement BFS**: Write a function `bfs_shortest_path(graph, start_node, end_node)` that performs a BFS traversal to find the shortest path.
    *   Use a queue (`collections.deque` is ideal, building on **Chunk 12**) to keep track of nodes to visit.
    *   Keep track of visited nodes to avoid cycles and redundant processing.
    *   Store the path by tracking the parent of each node as you visit it.
3.  **Reconstruct and Return Path**: Once the `end_node` is reached, reconstruct the path from `end_node` back to `start_node` using the parent pointers. Return the path as a list of user names.

**Relevant Sources & Theory**:
*   **Source**: `IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/20_Chapter_20_Elementary_Graph_Algorithms.pdf`
    *   **Theory**: Section 20.1 ("Representations of graphs") describes the adjacency-list representation. Section 20.2 ("Breadth-first search") details the BFS algorithm, proving that it finds the shortest-path distance in terms of the number of edges. Your implementation should follow the `BFS` pseudocode.
*   **Source**: `MathematicsForComputerScience_Lehman-Leighton-Meyer_2015/15_12_Simple_Graphs.pdf`
    *   **Theory**: Chapter 12 provides a high-level understanding of simple graphs and connectivity, which is the problem domain you are modeling. It helps contextualize *why* BFS is a suitable tool for this type of network analysis.

**Software Engineering Principles**:
*   **Efficiency**: BFS is the optimal algorithm for finding the shortest path in an unweighted graph, running in O(V + E) time. This is a crucial choice for efficiency.
*   **Scalability**: Adjacency lists are space-efficient for sparse graphs (like most social networks), making the solution scalable to larger datasets compared to an adjacency matrix.

---

# Exercise 3: Weighted Shortest Path with Dijkstra's Algorithm

**Objective**: Solve a single-source shortest path problem on a weighted graph using Dijkstra's algorithm. This exercise introduces the concept of path cost (not just hops) and requires using a priority queue for an efficient implementation.

**Problem Description**: A logistics company needs to find the fastest delivery routes from its main warehouse ('A') to all other distribution centers. The network is represented as a weighted directed graph where edge weights are the travel times in hours.

**Artificial Data**:
*   A set of distribution centers: `nodes = ["A", "B", "C", "D", "E", "F"]`
*   A list of one-way routes with travel times: `routes = [("A", "B", 7), ("A", "C", 9), ("A", "F", 14), ("B", "C", 10), ("B", "D", 15), ("C", "D", 11), ("C", "F", 2), ("D", "E", 6), ("E", "F", 9)]`

**Tasks**:
1.  **Represent the Weighted Graph**: Use an adjacency list (a dictionary) where keys are source nodes and values are lists of tuples, with each tuple containing `(destination_node, weight)`.
2.  **Implement Dijkstra's Algorithm**: Write a function `dijkstra(graph, start_node)` that computes the shortest travel time from `start_node` to every other node.
    *   Use a priority queue to efficiently retrieve the unvisited node with the smallest distance. Python's `heapq` module is perfect for this.
    *   Store the minimum distances in a dictionary or array.
    *   Store the predecessors (parents) to allow for path reconstruction.
3.  **Output the Results**: The function should return two dictionaries: one mapping each node to its shortest distance from the start, and another mapping each node to its predecessor in the shortest path.

**Relevant Sources & Theory**:
*   **Source**: `IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/22_Chapter_22_Single-Source_Shortest_Paths.pdf`
    *   **Theory**: Section 22.3 ("Dijkstra's algorithm") provides the complete theory, pseudocode, and correctness proof. The algorithm's greedy approach of always selecting the "closest" unvisited vertex is the central concept.
*   **Source**: URL [GeeksforGeeks: Dijkstra's Algorithm](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
    *   **Theory**: Provides a practical, implementation-focused explanation that complements the theoretical treatment in Cormen et al.
*   **Source**: URL [Python `heapq` documentation](https://docs.python.org/3/library/heapq.html)
    *   **Theory**: `heapq` is a min-heap implementation, which is the data structure that makes Dijkstra's algorithm efficient (O(E log V)). This connects the algorithm to underlying data structure choices.

**Software Engineering Principles**:
*   **Efficiency**: Implementing Dijkstra's with a binary heap (`heapq`) is far more efficient on sparse graphs than a simple array-based priority queue (O(V^2)). This choice is critical for performance on large graphs.
*   **Reliability**: Dijkstra's algorithm is guaranteed to find the optimal shortest path given the constraint of non-negative edge weights, making the solution reliable.

---

# Exercise 4: Advanced Tree Logic - Lowest Common Ancestor (LCA)

**Objective**: Implement an algorithm to find the Lowest Common Ancestor (LCA) of two nodes in a binary tree. This problem tests your ability to navigate tree structures and apply recursive logic to solve non-trivial path-based queries.

**Problem Description**: In a file system represented as a directory tree, the LCA of two files/folders represents the smallest directory that contains both of them. This is useful for determining permissions or finding the most specific shared path.

**Artificial Data**:
A binary tree structure (note: this is **not** a BST). Construct this tree manually.
*   Root: `_`
*   Children of `/`: `usr`, `etc`
*   Children of `usr`: `local`, `bin`
*   Children of `local`: `share`, `lib`
*   Children of `etc`: `network`, `init.d`
*   Find the LCA of `share` and `lib`.
*   Find the LCA of `lib` and `init.d`.

**Tasks**:
1.  **Build the Tree**: Manually construct the binary tree using the `TreeNode` class from Exercise 1.
2.  **Implement Recursive LCA**: Write a function `find_lca(root, node1, node2)`. The recursive logic is as follows:
    *   Base case: If the current node is `None` or matches one of the target nodes, return the current node.
    *   Recursive step: Search for the nodes in the left and right subtrees.
    *   Logic:
        *   If the recursive calls on both left and right subtrees return a non-null node, then the current node is the LCA.
        *   Otherwise, if only one of them returns a non-null node, that returned node is the LCA (or contains the LCA).

**Relevant Sources & Theory**:
*   **Source**: `DiscreteMathematicsandItsApplications_KennethHRosen_2018/18_Chapter_11_Trees.pdf`
    *   **Theory**: This chapter's concepts of `parent`, `ancestor`, and `descendant` (Section 11.1) are the formal definitions underlying the LCA problem. The solution relies on a recursive DFS-style traversal (Section 11.3) of the tree.
*   **Source**: **Pattern Recognition**: The **recursive tree processing pattern** is central here. The solution elegantly uses the call stack to trace paths and identify the fork point where the paths to the two nodes diverge, which is the LCA.

**Software Engineering Principles**:
*   **Efficiency**: The recursive solution traverses each node at most once, resulting in an efficient O(N) time complexity, where N is the number of nodes in the tree.
*   **Modifiability**: The function is self-contained and operates on a standard tree interface (`TreeNode`), making it reusable for any binary tree structure.

---

# Exercise 5: Hardcore Combined Problem - Multi-Modal Transit Network Optimization

**Objective**: Synthesize all concepts from this chunk to build a sophisticated routing algorithm. You will model a complex network, apply different shortest-path algorithms based on different optimization criteria (hops vs. time), and use tree-based logic (LCA) to analyze the resulting paths.

**Problem Description**: You are designing an intelligent transit app for a city. The transit system is a mix of fast subways, medium-speed buses, and slow walking paths. It is modeled as a single, large, weighted, directed graph where nodes are locations and edges are transit legs with a travel time weight. A user wants to travel from a `start_node` to an `end_node`. Your algorithm must provide two "best" routes:
1.  **The Quickest Route**: The path with the minimum possible travel time.
2.  **The Simplest Route**: The path with the minimum number of transfers/legs.

After finding these two distinct optimal paths, your algorithm must identify the **Critical Transfer Point**: the last common location shared by both paths before they diverge permanently. This point is conceptually the LCA of the two destinations within a combined path structure.

**Artificial Data**:
*   `nodes = ["Home", "BusStopA", "BusStopB", "Subway1", "Subway2", "Subway3", "Work", "CrossroadX"]`
*   `edges = [ # (source, dest, time_in_minutes)
      ("Home", "BusStopA", 5), ("Home", "CrossroadX", 10), ("CrossroadX", "Subway1", 8),
      ("BusStopA", "BusStopB", 10), ("BusStopB", "Subway2", 7), ("Subway1", "Subway2", 4),
      ("Subway2", "Subway3", 4), ("Subway3", "Work", 6), ("BusStopB", "Work", 25)
    ]`
*   `start_node = "Home"`, `end_node = "Work"`

**Tasks**:
1.  **Graph Representation**: Represent the transit system as a weighted directed graph using an **adjacency list**.
2.  **Find Simplest Route (Min Hops)**: Use **BFS** to find the shortest path from `start_node` to `end_node`. For BFS, treat the graph as unweighted (each edge has a cost of 1). Reconstruct and store this path.
    *   *Leveraged Property*: BFS is optimal for unweighted shortest paths. By ignoring weights, we correctly model "simplest" as fewest edges.
3.  **Find Quickest Route (Min Time)**: Use **Dijkstra's algorithm** with a min-heap to find the shortest path based on travel time. Reconstruct and store this path along with the parent pointers that form the shortest-path tree.
    *   *Leveraged Property*: Dijkstra's algorithm is optimal for weighted shortest paths with non-negative weights, correctly modeling the "quickest" route.
4.  **Find Critical Transfer Point**:
    *   The parent pointers from Dijkstra's algorithm form a shortest-path tree.
    *   Take the two paths found in steps 2 and 3. Trace them backward from `Work` to `Home`.
    *   The last common node you encounter when tracing back from `Work` is the Critical Transfer Point. Implement a function to find this. This function leverages the same logic as **LCA**: finding the "lowest" (in this case, "latest") common ancestor in the path structure.

**Relevant Sources & Theory**:
*   **Source**: `IntroductionToAlgorithms_Cormen-et-al_2022_FourthEdition/20_Chapter_20...` and `22_Chapter_22...`
    *   **Theory**: This problem directly contrasts the use cases of BFS (Section 20.2) and Dijkstra (Section 22.3). It shows that "shortest path" is context-dependent and requires choosing the right algorithm. The predecessor subgraph (`π` attributes) generated by these algorithms is a tree, which is the key **relationship** that enables the final analysis step.
*   **Source**: `DiscreteMathematicsandItsApplications_KennethHRosen_2018/18_Chapter_11_Trees.pdf`
    *   **Theory**: The concept of a path in a tree being unique from the root is fundamental. The parent pointers from BFS/Dijkstra form a shortest-path tree, allowing us to apply tree-based reasoning (like LCA) to a graph problem.

**Software Engineering Principles**:
*   **Efficiency & Scalability**: The solution uses the most efficient known algorithms for its subproblems (BFS is O(V+E), Dijkstra is O(E log V)). The adjacency list representation ensures it scales well.
*   **Reliability**: The algorithm is reliable because its components (BFS, Dijkstra) are proven to be correct under the given constraints (unweighted and non-negative weighted graphs, respectively).
*   **Meaningful Abstraction**: The final step of identifying the "Critical Transfer Point" shows how to transform the raw output of standard algorithms into a high-level, human-understandable insight, a key skill in software engineering.