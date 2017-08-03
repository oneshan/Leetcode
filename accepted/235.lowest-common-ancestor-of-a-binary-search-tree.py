#
# [235] Lowest Common Ancestor of a Binary Search Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
#
# Easy (38.79%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1]\nnode with value 2\nnode with value 1'
#
#
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of
# two given nodes in the BST.
#
#
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes v and w as the lowest node in T that has both v
# and w as descendants (where we allow a node to be a descendant of
# itself).”
#
#
#
# ⁠       _______6______
# ⁠      /              \
# ⁠   ___2__          ___8__
# ⁠  /      \        /      \
# ⁠  0      _4       7       9
# ⁠        /  \
# ⁠        3   5
#
#
#
# For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another
# example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of
# itself according to the LCA definition.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < root.val < q.val:
            return root
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode, TreeNode
        sol = Solution()
        root = createTreeNode([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        print(sol.lowestCommonAncestor(root, TreeNode(3), TreeNode(5)).val == 4)
        print(sol.lowestCommonAncestor(root, TreeNode(0), TreeNode(5)).val == 2)
        print(sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val == 6)
    except Exception as e:
        print(e)

