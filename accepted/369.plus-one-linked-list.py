#
# [369] Plus One Linked List
#
# https://leetcode.com/problems/plus-one-linked-list
#
# algorithms
# Medium (54.69%)
# Total Accepted:    18K
# Total Submissions: 33K
# Testcase Example:  '[1,2,3]'
#
# Given a non-negative integer represented as non-empty a singly linked list of
# digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
#
# The digits are stored such that the most significant digit is at the head of
# the list.
#
# Example:
#
# Input:
# 1->2->3
#
# Output:
# 1->2->4
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = curr = dummy
        while curr.next:
            if curr.next.val == 9:
                prev, curr = curr, curr.next
                while curr.next and curr.next.val == 9:
                    curr = curr.next
            else:
                curr = curr.next
        if curr.val < 9:
            curr.val += 1
        else:
            prev.val += 1
            curr = prev.next
            while curr:
                curr.val = 0
                curr = curr.next

        return dummy if dummy.val else head
