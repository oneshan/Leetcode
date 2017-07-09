#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
#
# Medium (29.27%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p1, p2 = dummy, head
        while p2:
            while p2.next and p2.val == p2.next.val:
                p2 = p2.next
            if p1.next == p2:
                p1 = p1.next
            else:
                p1.next = p2.next
            p2 = p2.next
        return dummy.next

if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()
        head = createListNode([1, 2, 3, 3, 4, 4, 5])
        printListNode(sol.deleteDuplicates(head))
        head = createListNode([1, 1, 1, 2, 3])
        printListNode(sol.deleteDuplicates(head))
    except Exception as e:
        print(e)
        pass
