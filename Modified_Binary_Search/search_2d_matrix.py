"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # Start at top-right corner
        row = 0
        col = len(matrix[0]) - 1  # Last column (rightmost)

        # Continue while we're within matrix bounds
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]

            # Found the target
            if current == target:
                return True

            # Current is too large, target must be to the left
            # Eliminate this column (current is smallest in its column)
            elif target < current:
                col -= 1

            # Current is too small, target must be below
            # Eliminate this row (current is largest in its row)
            else:
                row += 1

        # Traversed entire search space without finding target
        return False


"""
1. Pattern Recognition
Pattern: Search Space Reduction / Elimination Algorithm
Key Characteristics:
2D matrix with sorted rows AND sorted columns
Need to search for a target value efficiently
Can make decisions that eliminate entire rows or columns
Properties allow for directional movement based on comparisons
Better than brute force but not traditional binary search
Similar Problems:
LC 74: Search a 2D Matrix (fully sorted, can use true binary search)
LC 378: Kth Smallest Element in a Sorted Matrix
LC 668: Kth Smallest Number in Multiplication Table
Any problem with partially ordered 2D structures
2. High-Level Approach
Start at the top-right corner (or bottom-left), which has special properties: it's the largest in its row and smallest in its column. Compare the current element with the target to decide whether to eliminate the current row (move down) or eliminate the current column (move left). Continue until the target is found or you run out of bounds.
3. Step-by-Step Logic
Initialize position at top-right corner: row = 0, col = last column


Why: This position is the largest in its row and smallest in its column, giving us elimination power in both directions
Compare current element with target:


Why: This comparison tells us which entire row or column we can safely eliminate
If current > target:


Move left (col -= 1) to eliminate the current column
Why: Current is the SMALLEST in its column, so everything below is even larger. Target can't be in this column.
If current < target:


Move down (row += 1) to eliminate the current row
Why: Current is the LARGEST in its row, so everything to the left is even smaller. Target can't be in this row.
If current == target:


Return True - found it!
Why: Direct match
Continue until out of bounds:


If row >= m or col < 0, target doesn't exist
Why: We've eliminated all possible locations
4. Key Insights & Edge Cases
What Makes This Work:
The top-right (or bottom-left) corner has unique properties that allow bidirectional elimination
Each comparison eliminates an entire row OR column, not just one element
We're not doing binary search - we're doing systematic elimination
The sorted properties in both dimensions give us the power to make definitive elimination decisions
Implementation Details:
Must start at top-right or bottom-left (NOT top-left or bottom-right - those don't have the elimination properties)
Could also start at bottom-left with opposite movement logic (move right if too small, move up if too large)
Each step eliminates exactly one row or one column
No need to track visited positions - we never revisit
Edge Cases:
Empty matrix - return False immediately
Single element matrix - direct comparison
Target smaller than all elements - will traverse all the way left
Target larger than all elements - will traverse all the way down
Target exists multiple times - will find one occurrence
Matrix is 1×n or m×1 - degenerates to linear search
5. Pseudocode
function searchMatrix(matrix, target):
    if matrix is empty:
        return False
    
    row = 0
    col = last column index
    
    while row < num_rows AND col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        
        elif current > target:
            # Target must be to the left (eliminate column)
            col = col - 1
        
        else:  # current < target
            # Target must be below (eliminate row)
            row = row + 1
    
    return False  # Exhausted search space

6. Complexity Analysis
Time Complexity: O(m + n)
In worst case, traverse from top-right to bottom-left
Maximum m moves down + n moves left
Each step eliminates one row or one column
Not logarithmic because we eliminate one row/column at a time, not half
Space Complexity: O(1)
Only using two variables (row, col) to track position
No additional data structures
No recursion stack
Note: While O(m + n) is not logarithmic, it's still better than O(m log n) from binary searching each row when the matrix is large!
"""
