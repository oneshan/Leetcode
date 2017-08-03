#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list
#
# Easy (32.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Find the middle of linked list
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second-half of linked list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            curr, prev = temp, curr

        # Compare and check palindrome
        p1, p2 = head, prev
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


if __name__ == "__main__":
    try:
        from utils.ListNode import createListNode, printListNode
        sol = Solution()
        arr = createListNode([1, 2, 2, 1])
        print(sol.isPalindrome(arr) is True)
        arr = createListNode([1, 2, 3, 2, 1])
        print(sol.isPalindrome(arr) is True)
        arr = createListNode([1, 2, 3, 4, 2, 1])
        print(sol.isPalindrome(arr) is False)
    except Exception as e:
        print(e)
