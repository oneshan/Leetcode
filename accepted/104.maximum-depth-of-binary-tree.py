#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree
#
# Easy (52.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.maxLevel = 0
        self.recur(root, 1)
        return self.maxLevel

    def recur(self, node, level):
        self.maxLevel = max(self.maxLevel, level)
        if node.left:
            self.recur(node.left, level + 1)
        if node.right:
            self.recur(node.right, level + 1)

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, None, 2, 3])
        print(sol.maxDepth(root))
    except Exception as e:
        print(e)
