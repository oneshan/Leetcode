#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list
#
# Medium (24.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0'
#
# Given a list, rotate the list to the right by k places, where k is
# non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Get list size
        p2, size = dummy, 0
        while p2.next:
            p2 = p2.next
            size += 1

        # Update k
        k = (k - 1) % size + 1

        # Find last k-th node
        p1, p2 = dummy, dummy
        for i in range(k):
            p2 = p2.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        # Rotate
        if p1 != dummy:
            dummy.next = p1.next
            p1.next = None
            p2.next = head

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, printListNode, createListNode
        sol = Solution()
        arr = [1, 2, 3, 4, 5]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 1))

        arr = [1]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 1))

        arr = [1]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 99))

        arr = [1, 2]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 1))

        arr = [1, 2]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 2))

        arr = [1, 2]
        head = createListNode(arr)
        printListNode(sol.rotateRight(head, 3))

    except Exception as e:
        print(e)
        pass
