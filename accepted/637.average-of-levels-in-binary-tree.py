#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree
#
# Easy (55.53%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
#
# Example 1:
#
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
#
#
#
# Note:
#
# The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            _sum = 0
            for _ in range(size):
                node = queue.pop(0)
                _sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(_sum * 1.0 / size)
        return ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([3, 9, 20, 15, 7])
        print(sol.averageOfLevels(root) == [3, 14.5, 11])
    except Exception as e:
        print(e)
