""" 
Problem:
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

    Example 1:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
    
    Example 2:
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Solution:
    DFS through both trees and collect their leaf nodes. Then, check if both trees' leaf nodes are identical.

Complexity:
    Time: O(n)
    Space: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        # DFS to find all leaf nodes of a given tree
        def dfs(node):

            # Return empty list if there isn't a node
            if not node:
                return []

            # Return the current node if it is a leaf node
            if not node.left and not node.right:
                return [node.val]

            # Combine leaf nodes from both subtrees
            return dfs(node.left) + dfs(node.right)

        # Compare leaf nodes from both trees
        return dfs(root1) == dfs(root2)
