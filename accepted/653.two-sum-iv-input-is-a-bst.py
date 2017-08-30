#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst
#
# Easy (50.80%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#
#
# Example 2:
#
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
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
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        self.arr = []
        self.inorder(root)
        p1, p2 = 0, len(self.arr) - 1
        while p1 < p2:
            if self.arr[p1] + self.arr[p2] < k:
                p1 += 1
            elif self.arr[p1] + self.arr[p2] > k:
                p2 -= 1
            else:
                return True
        return False

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        self.arr += node.val,
        self.inorder(node.right)
