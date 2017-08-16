#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers
#
# Easy (51.23%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
#
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all
# test cases.
#


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX_INT = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        while b != 0:
            _sum = (a ^ b) & MASK
            _carry = ((a & b) << 1) & MASK
            a, b = _sum, _carry
        return a if a <= MAX_INT else (~0 << 31) | a


if __name__ == "__main__":
    sol = Solution()
    assert(sol.getSum(1, 2) == 3)
    assert(sol.getSum(1, 3) == 4)
