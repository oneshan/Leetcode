#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii
#
# algorithms
# Hard (39.27%)
# Total Accepted:    19.3K
# Total Submissions: 49K
# Testcase Example:  '[1]\n0.000000\n1'
#
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.ans = []
        self.target = target
        self.size = k
        self.inorder(root)
        return self.ans

    def inorder(self, node):
        if node.left:
            self.inorder(node.left)

        if len(self.ans) < self.size:
            self.ans.append(node.val)
        elif abs(node.val - self.target) < abs(self.ans[0] - self.target):
            self.ans.pop(0)
            self.ans.append(node.val)
        else:
            return
 
        if node.right:
            self.inorder(node.right)
