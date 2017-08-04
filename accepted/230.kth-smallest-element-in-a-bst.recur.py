#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst
#
# Medium (43.43%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
#
# Note: 
# You may assume k is always valid, 1 ? k ? BST's total elements.
#
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.ans = 0
        self.count = 0

        def inorder(node):
            if node.left:
                inorder(node.left)
            self.count += 1
            if self.count == k:
                self.ans = node.val
                return
            if node.right:
                inorder(node.right)

        if not root:
            return 0
        inorder(root)
        return self.ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([4, 2, 6, 1, 3, 5, 7])
        print(sol.kthSmallest(root, 1) == 1)
        print(sol.kthSmallest(root, 2) == 2)
        print(sol.kthSmallest(root, 3) == 3)
        print(sol.kthSmallest(root, 4) == 4)
        print(sol.kthSmallest(root, 5) == 5)
    except Exception as e:
        print(e)
