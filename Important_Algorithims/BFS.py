"""
The breadth first search (BFS) is uysed ot explore nodes and edges of a graph.
It runs with a time complexity of O(V+E) and is often used as a building block in other algorithims
The BFS algorithim is particularly useful for one thing: finding the shortest path on unweighted graphs.
A BFS starts at some arbitraty node of a grpah and explores the neighbor nodes first, before moving to the next level neighbors.
Uses a queue to track which node to visit next. Upon reaching a new node the algorithim adds it to the queue to visit it later.
"""

from collections import deque


def bfs_tree(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def bfs_graph(start, graph):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
