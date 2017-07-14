#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree
#
# Easy (32.92%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        level = 0
        queue = [root]
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue += node.left,
                if node.right:
                    queue += node.right,
        return level


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, None, 3])
        print(sol.minDepth(root))
    except Exception as e:
        print(e)
