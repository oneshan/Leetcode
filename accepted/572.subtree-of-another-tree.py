#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree
#
# Easy (41.07%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
# Given tree t:
#
# ⁠  4 
# ⁠ / \
# ⁠1   2
#
# Return true, because t has the same structure and node values with a subtree
# of s.
#
#
# Example 2:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return false.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def preorder(node):
            if not node:
                return "$"
            return "#" + str(node.val) + preorder(node.left) + preorder(node.right)

        return preorder(t) in preorder(s)


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        s = createTreeNode([3, 4, 5, 1, 2])
        t = createTreeNode([4, 1, 2])
        print(sol.isSubtree(s, t) is True)
    except Exception as e:
        print(e)
