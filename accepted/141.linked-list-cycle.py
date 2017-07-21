#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle
#
# Easy (35.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False
