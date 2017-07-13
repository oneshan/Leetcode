#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal
#
# Medium (39.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        arr = []
        queue = [root]
        while queue:
            size = len(queue)
            arr.append([])
            for _ in range(size):
                node = queue.pop(0)
                arr[-1] += node.val,
                if node.left:
                    queue += node.left,
                if node.right:
                    queue += node.right,
        return arr

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([3, 9, 20, None, None, 15, 7])
        print(sol.levelOrder(root))
    except Exception as e:
        print(e)
