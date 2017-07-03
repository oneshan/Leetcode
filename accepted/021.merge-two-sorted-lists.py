#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists
#
# Easy (38.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2, curr = l2.next, curr.next
            else:
                curr.next = l1
                l1, curr = l1.next, curr.next

        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()

        l1 = createListNode([1, 3, 5, 7])
        l2 = createListNode([2, 4, 6, 8])
        printListNode(sol.mergeTwoLists(l1, l2))
    except:
        pass
