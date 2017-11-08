#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number
#
# algorithms
# Easy (39.99%)
# Total Accepted:    30K
# Total Submissions: 75K
# Testcase Example:  '"1"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# For example, the numbers "69", "88", and "818" are all strobogrammatic.
#


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        table = {'1': '1', '8': '8', '6': '9', '9': '6', '0': '0'}
        p1, p2 = 0, len(num) - 1
        while p1 <= p2:
            if num[p1] not in table:
                return False
            elif num[p2] != table[num[p1]]:
                return False
            p1 += 1
            p2 -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isStrobogrammatic('88') is True)
    assert(sol.isStrobogrammatic('818') is True)
    assert(sol.isStrobogrammatic('69') is True)
    assert(sol.isStrobogrammatic('5') is False)
