#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal
#
# Medium (44.55%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
#
#
# For example:
# Given binary tree {1,#,2,3},
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
#
#
# return [1,2,3].
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
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            ans += node.val,
            if node.right:
                stack += node.right,
            if node.left:
                stack += node.left,
        return ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = createTreeNode(arr)
        print(sol.preorderTraversal(root))
    except Exception as e:
        print(e)
