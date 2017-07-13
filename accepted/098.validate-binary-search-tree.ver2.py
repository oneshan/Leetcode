#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree
#
# Medium (23.07%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,3]'
#
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
#
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
# Example 1:
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Binary tree [2,1,3], return true.
#
#
# Example 2:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
#
# Binary tree [1,2,3], return false.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, float('-inf'), float('inf'))

    def check(self, node, minV, maxV):
        if not node:
            return True
        if node.val < minV or node.val > maxV:
            return False
        return (
            self.check(node.left, minV, node.val - 1) and
            self.check(node.right, node.val + 1, maxV)
        )

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        print(sol.isValidBST(None))         # True
        root = createTreeNode([1, 1])
        print(sol.isValidBST(root))         # False
        root = createTreeNode([1, None, 1])
        print(sol.isValidBST(root))         # False
        root = createTreeNode([1, 2, 3])
        print(sol.isValidBST(root))         # False
        root = createTreeNode([2, 1, 3])
        print(sol.isValidBST(root))         # True
    except Exception as e:
        print(e)
