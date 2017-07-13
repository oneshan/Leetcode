#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree
#
# Easy (38.35%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
# But the following [1,2,2,null,3,null,3]  is not:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recur(root, root)

    def recur(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.recur(p.left, q.right) and self.recur(p.right, q.left)

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 2, 3, 4, 4, 3])        # True
        print(sol.isSymmetric(root))
        root = createTreeNode([1, 2, 2, None, 3, None, 3])  # False
        print(sol.isSymmetric(root))
        root = createTreeNode([1, 2, 3, 3, None, 2, None])  # False
        print(sol.isSymmetric(root))
        root = createTreeNode([5, 4, 1, None, 1, None, 4, 2, None, 2, None])  # False
        print(sol.isSymmetric(root))
    except Exception as e:
        print(e)
