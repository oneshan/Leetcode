#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
#
# Medium (31.84%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        val = postorder.pop()
        index = inorder.index(val)

        root = TreeNode(val)
        root.right = self.buildTree(inorder[index + 1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root

if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, printTreeNode
        sol = Solution()
        inorder = [4, 2, 5, 1, 6, 3]
        postorder = [4, 5, 2, 6, 3, 1]
        printTreeNode(sol.buildTree(inorder, postorder))
    except Exception as e:
        print(e)
