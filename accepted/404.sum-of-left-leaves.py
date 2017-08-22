#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves
#
# Easy (46.84%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = 0
        stack = [(root, False)]
        while stack:
            node, isLeft = stack.pop()
            if not node.left and not node.right and isLeft:
                ans += node.val
            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

        return ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([3, 9, 20, None, None, 15, 7])
        print(sol.sumOfLeftLeaves(root) == 24)
        root = createTreeNode([1])
        print(sol.sumOfLeftLeaves(root) == 0)
    except Exception as e:
        print(e)
