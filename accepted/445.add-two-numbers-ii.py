#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii
#
# Medium (46.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        len1, len2 = 0, 0
        while p1 or p2:
            if p1:
                p1, len1 = p1.next, len1 + 1
            if p2:
                p2, len2 = p2.next, len2 + 1

        dummy = ListNode(0)
        curr = dummy
        size = max(len1, len2)
        while size:
            val = 0
            if size <= len1:
                val += l1.val
                l1 = l1.next
            if size <= len2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val)
            curr = curr.next
            size -= 1

        prev = dummy
        while prev:
            curr = prev.next
            while curr and curr.val == 9:
                curr = curr.next
            while prev != curr:
                if curr and curr.val > 9:
                    prev.val += 1
                    prev.next.val -= 10
                prev = prev.next

        if dummy.val:
            return dummy
        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()
        l1 = createListNode([7, 2, 4, 3])
        l2 = createListNode([5, 6, 4])
        printListNode(sol.addTwoNumbers(l1, l2))
    except Exception as e:
        print(e)
