#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers
#
# Medium (27.48%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
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
        dummy = ListNode(0)
        node = dummy
        carry = 0
        while l1 or l2:
            carry = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            node.next = ListNode(carry % 10)
            carry //= 10
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            node.next = ListNode(carry)

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()

        l1 = createListNode([5, 2, 4])
        l2 = createListNode([5, 7, 5, 9])
        sumList = sol.addTwoNumbers(l1, l2)
        printListNode(sumList)

        l1 = createListNode([5, 4, 3, 1])
        l2 = createListNode([5, 7, 5, 2])
        sumList = sol.addTwoNumbers(l1, l2)
        printListNode(sumList)
    except:
        pass
