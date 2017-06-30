#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree
#
# Easy (46.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# 
# Given two binary trees, write a function to check if they are equal or not.
# 
# 
# Two binary trees are considered equal if they are structurally identical and
# the nodes have the same value.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
