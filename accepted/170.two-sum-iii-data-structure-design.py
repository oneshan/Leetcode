#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design
#
# algorithms
# Easy (25.17%)
# Total Accepted:    31.3K
# Total Submissions: 124.2K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
#
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
#
#
#
# For example,
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#
#
#


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.table[number] = self.table.get(number, 0) + 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.table:
            target = value - key
            if target == key:
                if self.table[key] > 1:
                    return True
            elif target in self.table:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

if __name__ == "__main__":
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    assert(obj.find(4) is True)
    assert(obj.find(7) is False)
    obj = TwoSum()
    obj.add(0)
    assert(obj.find(0) is False)
