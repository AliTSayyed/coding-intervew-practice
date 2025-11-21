"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

"""

from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if not prerequisites:
            return True

        graph = defaultdict(list)
        courses = prerequisites

        # create an adjacency list because one course can have many pre reqs
        for a, b in courses:
            graph[a].append(b)

        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        states = [UNSEEN] * numCourses

        # take a node (key) and determine if there is a cycle
        # we know there is a cycle if we find a neighbor who is in the visiting state
        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            if state == VISITING:
                return False

            states[node] = VISITING
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            return True

        # check each node in the graph for a cycle detection
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


"""
1. Pattern Recognition
Pattern: DFS Cycle Detection with Three-State Coloring
Key Characteristics:
Dependency graph (prerequisites = directed edges)
Need to detect if ordering is possible (no circular dependencies)
"Can you complete all X" → cycle detection in directed graph
Similar Problems:
Course Schedule II (LC 210) - return the ordering
Alien Dictionary (LC 269)
Detect Cycle in Directed Graph
2. High-Level Approach
Build an adjacency list from prerequisites, then use DFS with three states (unseen, visiting, visited) to detect cycles. If any node is revisited while still in "visiting" state, a cycle exists and courses cannot be completed.
3. Step-by-Step Logic
Build adjacency list → convert edge list to graph representation
Track three states per node:
UNSEEN: not yet processed
VISITING: currently in DFS path (on recursion stack)
VISITED: fully explored, no cycle from this node
If we hit VISITING node → back edge → cycle → return False
If we hit VISITED node → already verified safe → return True
Run DFS from each node → handles disconnected components
4. Key Insights & Edge Cases
Key Insights:
Three states distinguish "currently exploring" from "done exploring"
VISITING = on current path = cycle if revisited
defaultdict(list) avoids KeyError for nodes with no outgoing edges
Edge Cases:
No prerequisites: return True
Self-loop [0,0]: cycle detected
Disconnected components: loop through all nodes
5. Pseudocode
function canFinish(numCourses, prerequisites):
    graph = build adjacency list
    states = [UNSEEN] * numCourses
    
    function dfs(node):
        if states[node] == VISITED: return True
        if states[node] == VISITING: return False  // cycle!
        
        states[node] = VISITING
        for each neighbor:
            if not dfs(neighbor): return False
        states[node] = VISITED
        return True
    
    for each course 0 to numCourses-1:
        if not dfs(course): return False
    return True

6. Complexity Analysis
Time Complexity: O(V + E)
V = numCourses, E = prerequisites
Each node visited once, each edge traversed once
Space Complexity: O(V + E)
Adjacency list: O(E)
States array: O(V)
Recursion stack: O(V) worst case

"""
