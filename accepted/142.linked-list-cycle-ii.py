#
# [142] Linked List Cycle II
#
# https://leetcode.com/problems/linked-list-cycle-ii
#
# Medium (31.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.
#
#
#
# Note: Do not modify the linked list.
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = p2 = head
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            if p1 == p2:
                break
        else:
            return None

        p2 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2
