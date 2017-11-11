#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value
#
# algorithms
# Easy (39.94%)
# Total Accepted:    40.6K
# Total Submissions: 101.8K
# Testcase Example:  '[1]\n4.428571'
#
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff, self.ans = float('inf'), root.val

        def search(node):
            d = abs(target - node.val)
            if d < self.diff:
                self.diff, self.ans = d, node.val
            if node.val < target and node.right:
                search(node.right)
            elif node.val > target and node.left:
                search(node.left)

        search(root)
        return self.ans
