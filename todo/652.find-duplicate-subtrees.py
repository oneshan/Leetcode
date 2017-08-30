#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees
#
# Medium (31.52%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,1]'
#
# 
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them. 
# 
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# 
# Example 1: 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# The following are two duplicate subtrees:
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# and
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        
