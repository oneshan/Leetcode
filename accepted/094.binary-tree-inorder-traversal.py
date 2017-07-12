#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal
#
# Medium (45.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
#
# For example:
# Given binary tree [1,null,2,3],
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
#
#
# return [1,3,2].
#
#
# Note: Recursive solution is trivial, could you do it iteratively?
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.ans = []

        def recur(node):
            if node.left:
                recur(node.left)
            self.ans += node.val,
            if node.right:
                recur(node.right)

        recur(root)
        return self.ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([1, None, 2, 3])
        printTreeNode(root)
        print(sol.inorderTraversal(root))
    except:
        pass
