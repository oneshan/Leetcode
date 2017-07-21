#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list
#
# Medium (25.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#
# You must do this in-place without altering the nodes' values.
#
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Find the middle node of list
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next

        # Reverse second-half list
        pre, curr = None, p2.next
        p2.next = None
        while curr:
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp

        # Merge
        p1, p2 = head, pre
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2

        # printListNode(head)


if __name__ == "__main__":
    try:
        from utils.ListNode import createListNode, printListNode
        sol = Solution()
        head = createListNode([1])
        sol.reorderList(head)
        head = createListNode([1, 2])
        sol.reorderList(head)
        head = createListNode([1, 2, 3, 4, 5, 6, 7])
        sol.reorderList(head)
        head = createListNode([1, 2, 3, 4, 5, 6])
        sol.reorderList(head)
    except Exception as e:
        print(e)
