#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list
#
# Medium (32.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
#
#
# You should preserve the original relative order of the nodes in each of the
# two partitions.
#
#
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(0)
        h2 = ListNode(0)
        p1, p2 = h1, h2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = h2.next
        p2.next = None
        return h1.next

if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()
        head = createListNode([1, 4, 3, 2, 5, 2])
        printListNode(sol.partition(head, 3))
        printListNode(sol.partition(None, 3))
    except:
        pass
