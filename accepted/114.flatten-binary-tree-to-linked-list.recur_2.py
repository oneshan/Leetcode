#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
#
# Medium (34.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a binary tree, flatten it to a linked list in-place.
#
#
#
# For example,
# Given
#
# ⁠        1
# ⁠       / \
# ⁠      2   5
# ⁠     / \   \
# ⁠    3   4   6
#
#
#
# The flattened tree should look like:
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠     \
# ⁠      3
# ⁠       \
# ⁠        4
# ⁠         \
# ⁠          5
# ⁠           \
# ⁠            6
#
#
# click to show hints.
#
# Hints:
# If you notice carefully in the flattened tree, each node's right child points
# to the next node of a pre-order traversal.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.last = None
        self.preorder(root)
        # printTreeNode(root)

    def preorder(self, node):
        if not node:
            return
        self.preorder(node.right)
        self.preorder(node.left)
        node.right = self.last
        node.left = None
        self.last = node

if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 4, 3])
        sol.flatten(root)
    except Exception as e:
        print(e)
