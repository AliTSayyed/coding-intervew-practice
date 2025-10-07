"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        result = []

        # define boundaries
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            # traverse right along the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # move top boundary down

            # Traverse down along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # move right boundary left

            # Traverse left along the bottom row (if we still have rows)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
            bottom -= 1  # move bottom boundary up

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        return result


"""
Track 4 boundaries: top, bottom, left, right
Move in spiral order:

Right: From left to right on top row, then move top to bottom 
Down: From top to bottom on right column, then move right to left
Left: From right to left on bottom row, then move bottom to top
Up: From bottom to top on left column, then move left right


Shrink boundaries after each direction
Continue until boundaries cross
Let me break down the boundary logic step by step.
Initial Boundary Values:
m, n = len(matrix), len(matrix[0])  # m = rows, n = columns

top = 0        # First row index
bottom = m - 1 # Last row index  
left = 0       # First column index
right = n - 1  # Last column index

For matrix [[1,2,3],[4,5,6],[7,8,9]]:
m = 3, n = 3
top = 0, bottom = 2, left = 0, right = 2
This creates a "box" around the entire matrix:
   left=0  right=2
top=0   1    2    3
        4    5    6  
bottom=2 7   8    9

Boundary Shrinking Process:
Let me trace through each step:
Iteration 1:
Step 1 - Go Right (top row):
for col in range(left, right + 1):  # range(0, 3) = [0,1,2]
    result.append(matrix[top][col])  # matrix[0][0,1,2] = [1,2,3]
top += 1  # top becomes 1

Visits: [1,2,3]
Shrink: Top boundary moves down (we've "used up" row 0)
Step 2 - Go Down (right column):
for row in range(top, bottom + 1):  # range(1, 3) = [1,2]
    result.append(matrix[row][right])  # matrix[1,2][2] = [6,9]
right -= 1  # right becomes 1

Visits: [6,9]
Shrink: Right boundary moves left (we've "used up" column 2)
Step 3 - Go Left (bottom row):
if top <= bottom:  # 1 <= 2 ✓
    for col in range(right, left-1, -1):  # range(1, -1, -1) = [1,0]
        result.append(matrix[bottom][col])  # matrix[2][1,0] = [8,7]
bottom -= 1  # bottom becomes 1

Visits: [8,7]
Shrink: Bottom boundary moves up (we've "used up" row 2)
Step 4 - Go Up (left column):
if left <= right:  # 0 <= 1 ✓
    for row in range(bottom, top-1, -1):  # range(1, 0, -1) = [1]
        result.append(matrix[row][left])  # matrix[1][0] = [4]
left += 1  # left becomes 1

Visits: [4]
Shrink: Left boundary moves right (we've "used up" column 0)
After iteration 1: result = [1,2,3,6,9,8,7,4] New boundaries: top=1, bottom=1, left=1, right=1
Iteration 2:
Step 1 - Go Right:
for col in range(1, 1+1):  # range(1,2) = [1]
    result.append(matrix[1][1])  # matrix[1][1] = [5]
top += 1  # top becomes 2

Visits: [5]
Check loop condition: top <= bottom → 2 <= 1 → False!
Loop exits, return [1,2,3,6,9,8,7,4,5]
Visual representation of shrinking:
Initial:           After iteration 1:    After going right:
┌─────────────┐    ┌─────────────┐      ┌─────────────┐
│ 1 → 2 → 3 │    │ X   X   X │      │ X   X   X │
│ ↑       ↓ │    │ X   5   X │      │ X   X   X │
│ 4 ← 7 ← 8 │    │ X   X   X │      │ X   X   X │
└─────────────┘    └─────────────┘      └─────────────┘

Key insights:
Boundaries represent unvisited area - they shrink inward as we visit elements
Each direction "consumes" one boundary - after going right, we'll never revisit that top row
Termination condition - when boundaries cross (top > bottom or left > right), we've visited everything
Edge case checks - the if statements prevent revisiting elements in single-row or single-column cases
The boundaries essentially create a "shrinking rectangle" that guides our spiral path!

"""
