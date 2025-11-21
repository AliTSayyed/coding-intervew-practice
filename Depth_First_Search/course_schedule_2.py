"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

"""

from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        order = []
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(i):
            if states[i] == VISITED:
                return True
            if states[i] == VISITING:
                return False

            states[i] = VISITING
            for neighbor in graph[i]:
                if not dfs(neighbor):
                    return False
            states[i] = VISITED
            # After checking neighbors and determining no cycle, it means the course should be taken
            # All prerequisites (neighbors) are added to the order first
            # No cycle was detected in the subtree
            # Current course is safe to take
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order


"""
1. Pattern Recognition
Pattern: DFS Topological Sort with Cycle Detection
Key Characteristics:
Return valid ordering of dependencies
Directed graph where edges represent "must come before"
Need both cycle detection AND ordering
Similar Problems:
Course Schedule I (LC 207)
Alien Dictionary (LC 269)
Build Order (CTCI)
2. High-Level Approach
Use DFS with three-state coloring to detect cycles. Append each node to the result after all its dependencies are processed, naturally building a valid topological order.
3. Step-by-Step Logic
Build adjacency list → course points to its prerequisites
DFS with three states → detect cycles (VISITING hit twice = cycle)
Append node after recursion → ensures dependencies added first
Run DFS from all nodes → handles disconnected components
Return empty if cycle → no valid ordering exists
4. Key Insights & Edge Cases
Key Insights:
Post-order append = reverse topological order (dependencies first)
Graph direction: graph[course] = [prerequisites] means prereqs added before course
Edge Cases:
No prerequisites: return [0, 1, ..., n-1] (any order)
Cycle exists: return []
Disconnected courses: handled by looping all nodes
5. Pseudocode
function findOrder(numCourses, prerequisites):
    graph = build adjacency list
    states = [UNVISITED] * numCourses
    order = []
    
    function dfs(node):
        if VISITED: return True
        if VISITING: return False  // cycle
        
        states[node] = VISITING
        for neighbor in graph[node]:
            if not dfs(neighbor): return False
        states[node] = VISITED
        order.append(node)  // post-order
        return True
    
    for each course:
        if not dfs(course): return []
    return order

6. Complexity Analysis
Time: O(V + E) - each node/edge visited once
Space: O(V + E) - graph storage + recursion stack
"""
