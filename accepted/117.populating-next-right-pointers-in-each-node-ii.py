#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
#
# Medium (33.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '{}'
#
# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? Would your previous solution
# still work?
# 
# Note:
# You may only use constant extra space.
# 
# 
# For example,
# Given the following binary tree,
# 
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \    \
# ⁠   4   5    7
# 
# 
# 
# After calling your function, the tree should look like:
# 
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \    \
# ⁠   4-> 5 -> 7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(0)
        while root:
            node = dummy
            while root:
                node.next = root.left
                node = node.next if node.next else node
                node.next = root.right
                node = node.next if node.next else node
                root = root.next
            root = dummy.next
