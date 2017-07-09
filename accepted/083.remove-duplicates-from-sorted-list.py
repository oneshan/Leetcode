#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list
#
# Easy (39.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
#
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        node = head
        while node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head

if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()
        head = createListNode([1, 1, 2, 2, 3])
        printListNode(sol.deleteDuplicates(head))
        head = createListNode([1, 2, 3])
        printListNode(sol.deleteDuplicates(head))
        head = createListNode([1])
        printListNode(sol.deleteDuplicates(head))

    except:
        pass
