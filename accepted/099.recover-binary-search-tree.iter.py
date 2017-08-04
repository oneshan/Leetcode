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
        if not root:
            return

        prev = TreeNode(float('-inf'))
        n1, n2 = None, None
        stack = []

        node = root
        while node:
            stack.append(node)
            node = node.left

        while stack:
            node = stack.pop()
            if prev.val > node.val:
                if not n1:
                    n1 = prev
                n2 = node

            prev = node
            node = node.right
            while node:
                stack.append(node)
                node = node.left

        n1.val, n2.val = n2.val, n1.val
        # printTreeNode(root)


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([2, 3, 1])
        sol.recoverTree(root)
    except Exception as e:
        print(e)
