"""
A DFS plunges depth first into a graph without regard for which edge it takes next until it cannot go any gruther at which point it backtracks and continues
We can augemtn the DFS algorithim to
- Compute a graph's minimum spannign tree.
- Detect and find cycles in a graph.
- Check if a graph is a bipartite (a graph whose vertecies can be divided into two distinct independency sets such that now two verticeis within the same set are connected by an edge)
- Find strongly connected components.
- Topologically sort the nodes of a graph
- Find bridges and articulation points.
- Find augmenting paths in a flow network.
- Generate mazes.
"""


# first way to use dfs with recursion (easier way)
# on a tree structure do not need to use a vistied set
def dfs_tree(node):
    if not node:
        return
    print(node.value)
    dfs_tree(node.left)
    dfs_tree(node.right)


# second way to use dfs with a stack (manually keeping track of the call stack)
def dfs_iterative(start, graph):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        print(node.value)

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)


# graph dfs (recursion), need to keep track of a visited set because its a graph not a tree


def dfs_graph(node, graph, visited):
    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph(neighbor, graph, visited)
