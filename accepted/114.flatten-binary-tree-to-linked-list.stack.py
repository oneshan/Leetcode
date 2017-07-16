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
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack += node.right,
            if node.left:
                stack += node.left,
            if stack:
                node.right = stack[-1]
            node.left = None
        # printTreeNode(root)

if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 4, 3])
        sol.flatten(root)
    except Exception as e:
        print(e)
