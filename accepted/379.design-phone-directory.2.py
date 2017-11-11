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
from collections import deque


class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.table = {}
        self.numbers = deque()
        for i in range(maxNumbers):
            self.table[i] = True
            self.numbers.append(i)

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.numbers:
            return -1
        val = self.numbers.popleft()
        self.table[val] = False
        return val

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return self.table.get(number, False)

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not self.table[number]:
            self.numbers.append(number)
            self.table[number] = True

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
