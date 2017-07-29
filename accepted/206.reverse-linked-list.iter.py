#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list
#
# Easy (45.05%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Reverse a singly linked list.
#
# click to show more hints.
#
# Hint:
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        curr = None
        while head:
            temp = head.next
            head.next = curr
            curr, head = head, temp
        return curr


if __name__ == "__main__":
    try:
        from utils.ListNode import createListNode, printListNode
        sol = Solution()
        head = createListNode([1, 2, 3, 4, 5])
        printListNode(sol.reverseList(head))
    except Exception as e:
        print(e)
