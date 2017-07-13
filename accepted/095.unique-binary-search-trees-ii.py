#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii
#
# Medium (31.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1...n.
#
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.genBST(1, n)

    def genBST(self, left, right):
        arr = []
        if left > right:
            arr += None,
            return arr

        for i in range(left, right + 1):
            leftTree = self.genBST(left, i - 1)
            rightTree = self.genBST(i + 1, right)
            for lTree in leftTree:
                for rTree in rightTree:
                    root = TreeNode(i)
                    root.left = lTree
                    root.right = rTree
                    arr += root,
        return arr


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, createTreeNode, printTreeNode
        sol = Solution()
        for root in sol.generateTrees(3):
            printTreeNode(root)
    except Exception as e:
        print(e)
        pass
