#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Easy (41.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
