#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value
#
# Medium (55.67%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,3]'
#
#
# Given a binary tree, find the leftmost value in the last row of the tree. 
#
#
# Example 1:
#
# Input:
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Output:
# 1
#
#
#
# ⁠ Example 2: 
#
# Input:
#
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
#
# Output:
# 7
#
#
#
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = None
        queue = [root]
        while queue:
            size = len(queue)
            if size:
                ans = queue[0].val
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


if __name__ == "__main__":
    try:
        from utils.TreeNode import createTreeNode
        sol = Solution()
        root = createTreeNode([1, 2, 3, 4, None, 5, 6, None, None, 7])
        print(sol.findBottomLeftValue(root) == 7)
    except Exception as e:
        print(e)
    
