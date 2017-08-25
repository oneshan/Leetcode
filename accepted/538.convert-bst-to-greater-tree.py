#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree
#
# Medium (52.98%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
#
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.val = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            node.val = self.val = self.val + node.val
            inorder(node.left)

        inorder(root)
        return root


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([5, 2, 13])
        printTreeNode(sol.convertBST(root))
    except Exception as e:
        print(e)
