#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
#
# Medium (31.86%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        val = preorder.pop(0)
        index = inorder.index(val)

        root = TreeNode(val)
        root.left = self.buildTree(preorder, inorder[:index])
        root.right = self.buildTree(preorder, inorder[index + 1:])
        return root


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, printTreeNode
        sol = Solution()
        preorder = [1, 2, 4, 5, 3, 6]
        inorder = [4, 2, 5, 1, 6, 3]
        printTreeNode(sol.buildTree(preorder, inorder))
    except Exception as e:
        print(e)
