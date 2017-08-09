#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list
#
# Medium (43.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,4,5,6,7,8]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
#
#
# Example:
# Given 1->2->3->4->5->NULL,
# return 1->3->5->2->4->NULL.
#
#
# Note:
# The relative order inside both the even and odd groups should remain as it
# was in the input. 
# The first node is considered odd, the second node even and so on ...
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        oddHead = head
        evenHead = head.next
        p1, p2 = oddHead, evenHead

        head = head.next.next
        while head and head.next:
            p1.next = head
            p2.next = head.next
            head = head.next.next

            p1 = p1.next
            p2 = p2.next

        if head and not head.next:
            p1.next = head
            p2.next = None
            p1 = p1.next

        p1.next = evenHead

        return oddHead


if __name__ == "__main__":
    try:
        from utils.ListNode import createListNode, printListNode
        sol = Solution()
        root = createListNode([1, 2, 3, 4, 5, 6, 7, 8])
        printListNode(sol.oddEvenList(root))
        root = createListNode([1, 2, 3, 4, 5, 6, 7])
        printListNode(sol.oddEvenList(root))
    except Exception as e:
        print(e)
