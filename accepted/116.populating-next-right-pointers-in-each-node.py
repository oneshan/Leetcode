#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node
#
# Medium (36.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '{}'
#
#
# Given a binary tree
#
# ⁠   struct TreeLinkNode {
# ⁠     TreeLinkNode *left;
# ⁠     TreeLinkNode *right;
# ⁠     TreeLinkNode *next;
# ⁠   }
#
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
# Note:
#
# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the
# same level, and every parent has two children).
#
#
#
#
# For example,
# Given the following perfect binary tree,
#
# ⁠        1
# ⁠      /  \
# ⁠     2    3
# ⁠    / \  / \
# ⁠   4  5  6  7
#
#
#
# After calling your function, the tree should look like:
#
# ⁠        1 -> NULL
# ⁠      /  \
# ⁠     2 -> 3 -> NULL
# ⁠    / \  / \
# ⁠   4->5->6->7 -> NULL
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
        if not root or not root.left:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


if __name__ == "__main__":
    pass
