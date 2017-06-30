#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree
#
# Hard (29.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,1]'
#
# 
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# 
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
