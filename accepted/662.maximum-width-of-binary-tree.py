#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree
#
# Medium (33.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null. 
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
#
# Example 1:
#
# Input: 
#
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
#
#
#
# Example 2:
#
# Input: 
#
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
#
#
#
# Example 3:
#
# Input: 
#
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
#
#
# Example 4:
#
# Input: 
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
#
#
#
#
# Note:
# Answer will in the range of 32-bit signed integer.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans = 0
        queue = [(1, root)]
        while queue:
            size = len(queue)
            left = right = None
            for _ in range(size):
                idx, node = queue.pop(0)
                if not left:
                    left = right = idx
                else:
                    right = idx
                if node.left:
                    queue.append((idx * 2, node.left))
                if node.right:
                    queue.append((idx * 2 + 1, node.right))
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    try:
        from utils.TreeNode import createTreeNode
        root = createTreeNode([1, 3, 2, 5, 3, None, 9])
        print(sol.widthOfBinaryTree(root) == 4)
    except Exception as e:
        print(e)
