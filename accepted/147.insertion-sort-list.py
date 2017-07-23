#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list
#
# Medium (32.81%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Sort a linked list using insertion sort.
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        dummy = ListNode(0)
        curr = dummy

        while head:
            if curr and curr.val > head.val:
                curr = dummy
            while curr.next and curr.next.val < head.val:
                curr = curr.next

            temp = curr.next
            curr.next = head
            head = head.next
            curr.next.next = temp

        return dummy.next


if __name__ == "__main__":
    try:
        from utils.ListNode import ListNode, createListNode, printListNode
        sol = Solution()
        head = createListNode([1, 3, 2, 4, 5])
        printListNode(sol.insertionSortList(head))
        head = createListNode([3, 4, 1])
        printListNode(sol.insertionSortList(head))
        head = createListNode([1, 1])
        printListNode(sol.insertionSortList(head))
    except Exception as e:
        print(e)
