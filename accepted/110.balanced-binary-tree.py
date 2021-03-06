#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree
#
# Easy (37.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, determine if it is height-balanced.
#
#
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.check(root) >= 0

    def check(self, node):
        if not node:
            return 0
        depth_left = self.check(node.left)
        depth_right = self.check(node.right)
        if depth_left < 0 or depth_right < 0 or abs(depth_left - depth_right) > 1:
            return -1
        return 1 + max(depth_left, depth_right)

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 3])
        print(sol.isBalanced(root))
        root = createTreeNode([1, None, 2, None, 3])
        print(sol.isBalanced(root))
    except Exception as e:
        print(e)
