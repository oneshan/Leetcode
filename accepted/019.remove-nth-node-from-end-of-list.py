#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
#
# Medium (33.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n1'
#
# Given a linked list, remove the nth node from the end of list and return its
# head.
#
#
# For example,
#
#
# ⁠  Given linked list: 1->2->3->4->5, and n = 2.
#
# ⁠  After removing the second node from the end, the linked list becomes
# 1->2->3->5.
#
#
#
# Note:
# Given n will always be valid.
# Try to do this in one pass.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        p1, p2 = head, dummy
        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()

        head = createListNode([1, 2, 3, 4, 5, 6, 7])
        printListNode(sol.removeNthFromEnd(head, 7))  # Remove head node
        printListNode(sol.removeNthFromEnd(head, 3))  # Remove middle node
        printListNode(sol.removeNthFromEnd(head, 1))  # Remove last node
    except:
        pass
