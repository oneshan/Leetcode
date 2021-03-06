#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number
#
# Easy (39.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '-2147483648'
#
#
# Write a program to check whether a given number is an ugly number.
#
#
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another
# prime factor 7.
#
#
#
# Note that 1 is typically treated as an ugly number.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        for prime in (2, 3, 5):
            while num % prime == 0:
                num /= prime
        return num == 1


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isUgly(1) is True)
    assert(sol.isUgly(14) is False)
    assert(sol.isUgly(12) is True)
