#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements
#
# Easy (32.08%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head

        current = dummy
        while current:
            while current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import createListNode, ListNode, printListNode
        sol = Solution()
        head = createListNode([1, 2, 6, 3, 4, 5, 6])
        printListNode(sol.removeElements(head, 6))
        printListNode(sol.removeElements(head, 1))
    except Exception as e:
        print(e)
