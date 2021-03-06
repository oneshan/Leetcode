#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum
#
# Easy (33.72%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n1'
#
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
#
#
# For example:
# Given the below binary tree and sum = 22,
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
#
#
#
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        stack = [(root, sum)]
        while stack:
            node, sum = stack.pop()
            if sum == node.val and not node.left and not node.right:
                return True
            if node.left:
                stack += (node.left, sum - node.val),
            if node.right:
                stack += (node.right, sum - node.val),
        return False

if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([5, 4, 8, 11, 13, 4, 7, 2, None, 1])
        print(sol.hasPathSum(root, 22))
        print(sol.hasPathSum(None, 22))
    except Exception as e:
        print(e)
