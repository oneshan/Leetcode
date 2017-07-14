#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
#
# Easy (41.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root


if __name__ == "__main__":
    try:
        from utils.TreeNode import TreeNode, printTreeNode
        sol = Solution()
        arr = [1, 2, 3, 4, 5, 6]
        printTreeNode(sol.sortedArrayToBST(arr))
    except Exception as e:
        print(e)
