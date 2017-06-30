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
        
