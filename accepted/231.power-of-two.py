#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two
#
# Easy (39.94%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
#
# Given an integer, write a function to determine if it is a power of two.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return n & (n - 1) == 0


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isPowerOfTwo(0) is False)
    assert(sol.isPowerOfTwo(1) is True)
    assert(sol.isPowerOfTwo(2) is True)
    assert(sol.isPowerOfTwo(3) is False)
    assert(sol.isPowerOfTwo(4) is True)
    assert(sol.isPowerOfTwo(5) is False)
