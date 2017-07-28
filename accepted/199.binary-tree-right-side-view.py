#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view
#
# Medium (40.27%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
#
# For example:
# Given the following binary tree,
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
#
#
#
# You should return [1, 3, 4].
#
#
# Credits:Special thanks to @amrsaqr for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if i == 0:
                    ans += node.val,
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        arr = [1, 2, 3, 4, 5]
        root = createTreeNode(arr)
        sol = Solution()
        print(sol.rightSideView(root))
    except Exception as e:
        print(e)
