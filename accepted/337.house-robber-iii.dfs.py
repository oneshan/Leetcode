#
# [337] House Robber III
#
# https://leetcode.com/problems/house-robber-iii
#
# Medium (43.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
#
# The thief has found himself a new place for his thievery again. There is only
# one entrance to this area, called the "root." Besides the root, each house
# has one and only one parent house. After a tour, the smart thief realized
# that "all houses in this place forms a binary tree". It will automatically
# contact the police if two directly-linked houses were broken into on the same
# night.
#
#
#
# Determine the maximum amount of money the thief can rob tonight without
# alerting the police.
#
#
# Example 1:
#
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
#
# Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
#
# Example 2:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
#
# Maximum amount of money the thief can rob = 4 + 5 = 9.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Bottom-up: dp[i] = max(dp[i-2] + node.val, dp[i-1])

        def dfs(node):
            if not node:
                return (0, 0)
            rob_l, pass_l = dfs(node.left)
            rob_r, pass_r = dfs(node.right)

            dp_1 = rob_l + rob_r
            dp_2 = pass_l + pass_r
            return max(dp_2 + node.val, dp_1), dp_1

        return dfs(root)[0]
