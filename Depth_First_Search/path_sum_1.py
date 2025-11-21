"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
"""


class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        # search down till a leaf node and check if the value at the point of a leaf is equal to target sum
        def dfs(node, val):
            if not node:
                return False

            val += node.val

            if not node.left and not node.right:
                return val == targetSum

            return dfs(node.left, val) or dfs(node.right, val)

        return dfs(root, 0)


"""
1. Pattern Recognition
Pattern: DFS with Accumulated State
Key Characteristics:
Root-to-leaf path traversal
Accumulate values along path
Check condition only at leaf nodes
Binary tree structure
Similar Problems:
Path Sum II (LC 113) - return all paths
Path Sum III (LC 437) - any path, not just root-to-leaf
Binary Tree Maximum Path Sum (LC 124)
2. High-Level Approach
Use DFS to traverse from root to each leaf, accumulating the sum along the path. At each leaf node, check if the accumulated sum equals the target. Return true if any path matches; false if all paths exhausted.
3. Step-by-Step Logic
Base case: null node → return False (no path here)


Add current node's value to running sum


WHY: Building path sum incrementally
Check if leaf node (no left AND no right child)


WHY: Only complete paths count; leaf = path end
Return whether accumulated sum equals target
Recurse on children with OR logic


WHY: Only need ONE valid path; short-circuits on first True
4. Key Insights & Edge Cases
Key Insights:
Leaf check: not node.left and not node.right (both must be None)
Pass accumulated value down, not remaining target (either works)
OR logic enables early termination on success
Edge Cases:
Empty tree: returns False
Single node (root is leaf): check root.val == targetSum
Negative values: handled naturally by addition
5. Pseudocode
function hasPathSum(root, targetSum):
    function dfs(node, currentSum):
        if node is null:
            return False
        
        currentSum += node.val
        
        if node is leaf:
            return currentSum == targetSum
        
        return dfs(node.left, currentSum) OR dfs(node.right, currentSum)
    
    return dfs(root, 0)

6. Complexity Analysis
Time Complexity: O(n)
Visit each node at most once
Space Complexity: O(h)
h = height of tree (recursion stack)
Worst: O(n) skewed tree
Best: O(log n) balanced tree
"""
