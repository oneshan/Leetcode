#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum
#
# Hard (25.79%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
# 
# Given a binary tree, find the maximum path sum.
# 
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# 
# For example:
# Given the below binary tree,
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 
# 
# Return 6.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('-inf')
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        left = left if left > 0 else 0
        right = self.traverse(node.right)
        right = right if right > 0 else 0
        self.ans = max(self.ans, node.val + left + right)
        return max(left, right) + node.val
