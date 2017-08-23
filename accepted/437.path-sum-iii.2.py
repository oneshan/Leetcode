#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii
#
# Easy (39.46%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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

    def __init__(self):
        self.ans = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0

        self.table = {0: 1}
        return self.recur(root, 0, sum)

    def recur(self, node, curr, sum):
        if not node:
            return 0

        curr += node.val
        count = self.table.get(curr - sum, 0)

        self.table[curr] = self.table.get(curr, 0) + 1
        count += self.recur(node.left, curr, sum)
        count += self.recur(node.right, curr, sum)
        self.table[curr] -= 1
        return count


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        root = createTreeNode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        sol = Solution()
        print(sol.pathSum(root, 8) == 3)
    except Exception as e:
        print(e)
