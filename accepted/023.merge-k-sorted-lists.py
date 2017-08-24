#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists
#
# Hard (26.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        minheap = []
        for head in lists:
            if head:
                heapq.heappush(minheap, (head.val, head))

        head = ListNode(0)
        curr = head
        while minheap:
            _, node = heapq.heappop(minheap)
            curr.next = node
            if node.next:
                heapq.heappush(minheap, (node.next.val, node.next))
            curr = curr.next

        return head.next
