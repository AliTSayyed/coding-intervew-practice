"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum: int):
        ret = []

        def dfs(node, path):
            if not node:
                return

            path.append(node.val)

            # if we are at a leaf node and check if path sum is target sum
            if not node.left and not node.right:
                if sum(path) == targetSum:
                    # add a copy of the path else path will be mutated
                    ret.append(path[:])

            # if not a leaf, explore left and right, if there is nothing,
            # backtrack: remove current node after exploring its subtrees
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()

        dfs(root, [])
        return ret
