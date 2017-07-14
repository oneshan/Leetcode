#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii
#
# Medium (33.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
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
# ⁠        /  \    / \
# ⁠       7    2  5   1
#
#
#
# return
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.traverse(root, sum, [])
        return self.ans

    def traverse(self, node, sum, arr):

        if not node:
            return

        if node.val == sum and not node.left and not node.right:
            self.ans.append(arr + [node.val])

        self.traverse(node.left, sum - node.val, arr + [node.val])
        self.traverse(node.right, sum - node.val, arr + [node.val])


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        print(sol.pathSum(root, 22))
    except Exception as e:
        print(e)
