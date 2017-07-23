#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal
#
# Hard (39.76%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
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
# return [3,2,1].
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ans = []
        self.traverse(root)
        return self.ans

    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        self.traverse(node.right)
        self.ans += node.val,


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = createTreeNode(arr)
        print(sol.postorderTraversal(root))
    except Exception as e:
        print(e)       
