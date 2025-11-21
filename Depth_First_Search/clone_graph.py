"""
Problem:
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Example 1:

Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # going to use a dict to store the new nodes mapped to their original
        old_to_new = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                # connect the neighbors to the new node created
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]


"""
1. Pattern Recognition
Pattern: Graph Traversal (DFS/BFS) + Hash Map for Node Mapping
Key Characteristics:
Deep copy of a data structure with circular references
Need to maintain identity mapping (original → clone)
Cycles in graph require visited tracking
Must preserve structure, not just values
Similar Problems:
Copy List with Random Pointer (LC 138)
Clone Binary Tree with Random Pointer (LC 1485)
Clone N-ary Tree (LC 1490)
2. High-Level Approach
Use a hash map to track original-to-clone mappings while traversing with DFS/BFS. For each node, create its clone (if new) and connect the clone's neighbors to the cloned versions of the original neighbors. The map serves double duty: prevents infinite loops in cycles and ensures each node is cloned exactly once.
3. Step-by-Step Logic
Handle null input → return None


Initialize map with starting node's clone


WHY: Need entry point; map tracks visited + stores clones
DFS/BFS traversal using stack


WHY: Must visit every node to clone it
For each neighbor of current node:


If not in map: create clone, add to map, add to stack
WHY: Only create each clone once
Connect clone's neighbors (always, not just if new)


WHY: Every edge must be copied; neighbor may be visited but not yet connected from this node
Return clone of starting node


WHY: Map gives us the cloned entry point
4. Key Insights & Edge Cases
Key Insights:
Map serves two purposes: visited set + clone storage
Neighbor connection is outside the if-statement (handles back-edges)
Create nodes with value only; neighbors built incrementally
Order: create clone first, then add to stack (ensures clone exists when connecting)
Edge Cases:
Null node: return None
Single node (no neighbors): works fine
Self-loop: handled by map check
Fully connected graph: all edges copied correctly
5. Pseudocode
function cloneGraph(node):
    if node is null:
        return null
    
    old_to_new = {node: new Node(node.val)}
    stack = [node]
    
    while stack not empty:
        curr = stack.pop()
        
        for each neighbor of curr:
            if neighbor not in old_to_new:
                old_to_new[neighbor] = new Node(neighbor.val)
                stack.push(neighbor)
            
            // Always connect (handles back-edges)
            old_to_new[curr].neighbors.append(old_to_new[neighbor])
    
    return old_to_new[node]

6. Complexity Analysis
Time Complexity: O(V + E)
Visit each node once: O(V)
Process each edge once: O(E)
Space Complexity: O(V)
Hash map stores V nodes
Stack holds at most V nodes
New graph is O(V + E) but typically not counted as auxiliary space

"""
