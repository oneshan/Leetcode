#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
#
# Medium (33.68%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = dummy, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        mid = p1.next
        p1.next = None
        root = TreeNode(mid.val)
        if head != mid:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(mid.next)
        return root

if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode
        from utils.TreeNode import TreeNode, printTreeNode
        sol = Solution()
        head = createListNode([1, 2, 3, 4, 5, 6])
        printTreeNode(sol.sortedListToBST(head))
    except Exception as e:
        print(e)
