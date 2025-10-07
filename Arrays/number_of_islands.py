import collections

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        # use this search alg to find all connected 1s
        # search broad then specific
        def bfs(r, c):
            pass
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = (
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1),
                )  # up down right left search directions allowed

                for dr, dc in directions:  # tuple unpacking
                    r, c = row + dr, col + dc  # temp search of new coordinate position

                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visit
                    ):
                        q.append(
                            (r, c)
                        )  # this makes it BFS, store in queue to search later not immediatley
                        visit.add(
                            (r, c)
                        )  # do not check coordiante again (counts as same island)

        # start iterating through the grid
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = (
            set()
        )  # use this to keep track of what coordinates have been visited with BFS

        # this is the overall iteration loop
        for r in range(rows):
            for c in range(cols):
                # if we have not come across this 1 before and the coordiante is not in visited set
                #  then BFS it
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    count += 1

        return count


"""
Use BFS. When you encounter a 1, store its position in visited and then use bfs to find all connected 1’s. After finding all corrected ones, increment the count by one. Continue this until all positions are checked. 
The more 1’s found the more positions are visited so you check less often as you iterate throughout the grid. O(M * N) time.
BFS (Queue - FIFO):
Process the oldest unvisited neighbors first
Explores level by level, like ripples in a pond
"Finish exploring all current neighbors before moving deeper"
DFS (Stack - LIFO):
Process the newest unvisited neighbors first
Dives deep immediately when it finds a new path
"Whenever you see something new, explore it right away"
DFS = Dog 🐕
Like a dog that sees a squirrel and immediately chases it down the deepest path
Gets distracted by the newest, most exciting thing
"Ooh, new path! Must explore NOW!"
BFS = Broad 📡
Explores broadly, spreading out in all directions evenly
Systematic and methodical, like radar scanning
"Let me check everything at this level before going deeper"
Number of Islands - BFS Solution Summary
Algorithm Overview:
Uses BFS (Breadth-First Search) to find connected components of land ('1') in a 2D grid. Each connected component = one island.
Key Strategy:
Scan the entire grid for unvisited land cells
When you find new land → start BFS to explore the entire island
Mark all connected land as visited to avoid double-counting
Increment island counter after each complete BFS
BFS Implementation:
Queue (deque): Stores coordinates to visit next
Directions tuple: ((1,0), (-1,0), (0,1), (0,-1)) for up/down/left/right movement
Visited set: Tracks (row, col) coordinates already explored
Boundary checking: Ensures we don't go out of grid bounds
Core Logic Flow:
For each cell in grid:
  If it's land ('1') AND not visited:
    → Run BFS to mark entire island as visited
    → Increment island count

Why BFS Works:
Explores level by level (like ripples in water)
Finds all connected land before moving to next island
Queue ensures breadth-first exploration vs depth-first
Time/Space:
Time: O(m×n) - visit each cell once
Space: O(m×n) - for visited set and queue in worst case
Key insight: Each BFS call discovers exactly one complete island!
"""
