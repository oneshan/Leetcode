#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree
#
# Hard (29.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,1]'
#
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a
# constant space solution?
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode(float('-inf'))
        self.res = [None, None]
        self.inorder(root)
        self.res[0].val, self.res[1].val = self.res[1].val, self.res[0].val
        # printTreeNode(root)

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)

        if self.prev.val > node.val:
            if not self.res[0]:
                self.res[0] = self.prev
            self.res[1] = node
        self.prev = node

        self.inorder(node.right)


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([2, 3, 1])
        sol.recoverTree(root)
    except Exception as e:
        print(e)
