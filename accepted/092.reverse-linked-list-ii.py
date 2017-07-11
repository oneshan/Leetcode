#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii
#
# Medium (30.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5]\n1\n1'
#
#
# Reverse a linked list from position m to n. Do it in-place and in
# one-pass.
#
#
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
#
# return 1->4->3->2->5->NULL.
#
#
# Note:
# Given m, n satisfy the following condition:
# 1 ? m ? n ? length of list.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # p1 points to (m-1)th node
        p1 = dummy
        for i in range(m - 1):
            p1 = p1.next

        # Reverse node from position m to n
        pre, curr = None, p1.next
        for i in range(n - m + 1):
            temp = curr.next
            curr.next = pre
            pre, curr = curr, temp

        # Let original mth node points to (n+1)th node
        p1.next.next = curr
        # Let original (m-1)th node points to nth node
        p1.next = pre
        return dummy.next

if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, printListNode, createListNode
        sol = Solution()
        head = createListNode([1, 2, 3, 4, 5])
        printListNode(sol.reverseBetween(head, 2, 4))   # 1 4 3 2 5
        head = createListNode([1, 2, 3, 4, 5])
        printListNode(sol.reverseBetween(head, 0, 3))
    except:
        pass
