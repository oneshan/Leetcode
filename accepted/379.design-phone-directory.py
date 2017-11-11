#
# [379] Design Phone Directory
#
# https://leetcode.com/problems/design-phone-directory
#
# algorithms
# Medium (33.88%)
# Total Accepted:    12K
# Total Submissions: 35.3K
# Testcase Example:  '["PhoneDirectory","get","get","check","get","check","release","check"]\n[[3],[],[],[2],[],[2],[2],[2]]'
#
# Design a Phone Directory which supports the following operations:
#
#
#
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
#
#
#
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);
#
#
#


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None
        self.valid = True


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.maxNumbers = maxNumbers
        self.table = {}
        self.head = ListNode(0)
        curr = self.head
        for i in range(maxNumbers):
            node = ListNode(i)
            curr.next, node.prev = node, curr
            curr = curr.next
            self.table[i] = node

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        node = self.head.next
        if not node:
            return -1

        self.head.next = node.next
        if node.next:
            node.next.prev = self.head
        node.prev = node.next = None
        node.valid = False
        return node.val

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0 <= number < self.maxNumbers and self.table[number].valid

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        node = self.table[number]
        if not node.valid:
            node.valid = True
            node.prev, node.next = self.head, self.head.next
            self.head.next = node

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

if __name__ == "__main__":
    obj = PhoneDirectory(3)
    assert(obj.get() == 0)
    assert(obj.check(2) is True)
    obj.release(2)
