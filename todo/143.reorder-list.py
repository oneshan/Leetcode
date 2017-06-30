#
# [143] Reorder List
#
# https://leetcode.com/problems/reorder-list
#
# Medium (25.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# 
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# 
# 
# You must do this in-place without altering the nodes' values.
# 
# 
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
