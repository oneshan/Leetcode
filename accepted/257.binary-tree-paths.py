#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths
#
# Easy (37.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,null,5]'
#
#
# Given a binary tree, return all root-to-leaf paths.
#
#
# For example, given the following binary tree:
#
#
#
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
#
#
#
# All root-to-leaf paths are:
# ["1->2->5", "1->3"]
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.ans = []
        self.traverse(root, "")
        return self.ans

    def traverse(self, node, path):
        path += "->{}".format(node.val)
        if not node.left and not node.right:
            self.ans += path[2:],
            return
        if node.left:
            self.traverse(node.left, path)
        if node.right:
            self.traverse(node.right, path)


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 3, None, 5])
        print(sol.binaryTreePaths(root))
    except Exception as e:
        print(e)
