#
# [508] Most Frequent Subtree Sum
#
# https://leetcode.com/problems/most-frequent-subtree-sum
#
# Medium (52.21%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,2,-3]'
#
#
# Given the root of a tree, you are asked to find the most frequent subtree
# sum. The subtree sum of a node is defined as the sum of all the node values
# formed by the subtree rooted at that node (including the node itself). So
# what is the most frequent subtree sum value? If there is a tie, return all
# the values with the highest frequency in any order.
#
#
# Examples 1
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -3
#
# return [2, -3, 4], since all the values happen only once, return all of them
# in any order.
#
#
# Examples 2
# Input:
#
# ⁠ 5
# ⁠/  \
# 2   -5
#
# return [2], since 2 happens twice, however -5 only occur once.
#
#
# Note:
# You may assume the sum of values in any subtree is in the range of 32-bit
# signed integer.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.table = {}
        self.maxCount = 0
        self.recur(root)
        return [val for val in self.table if self.table[val] == self.maxCount]

    def recur(self, node):
        if not node:
            return 0
        val = node.val + self.recur(node.left) + self.recur(node.right)
        self.table[val] = self.table.get(val, 0) + 1
        self.maxCount = max(self.maxCount, self.table[val])
        return val


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([5, 2, -3])
        print(sol.findFrequentTreeSum(root) == [2, -3, 4])
        root = createTreeNode([5, 2, -5])
        print(sol.findFrequentTreeSum(root) == [2])
    except Exception as e:
        print(e)
