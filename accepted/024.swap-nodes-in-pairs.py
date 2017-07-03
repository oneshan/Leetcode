#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs
#
# Medium (38.06%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a linked list, swap every two adjacent nodes and return its head.
#
#
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#
#
# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr.next and curr.next.next:
            p1, p2 = curr.next, curr.next.next
            p1.next = p2.next
            p2.next = p1
            curr.next = p2
            curr = curr.next.next

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()

        head = createListNode([1])
        printListNode(sol.swapPairs(head))

        head = createListNode([1, 2])
        printListNode(sol.swapPairs(head))

        head = createListNode([1, 2, 3, 4, 5, 6, 7])
        printListNode(sol.swapPairs(head))  # Odd case

        head = createListNode([1, 2, 3, 4, 5, 6])
        printListNode(sol.swapPairs(head))  # Even case

    except:
        pass
