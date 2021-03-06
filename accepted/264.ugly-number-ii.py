#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii
#
# Medium (32.32%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
#
# Write a program to find the n-th ugly number.
#
#
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
#
#
# Note that 1 is typically treated as an ugly number, and n does not exceed
# 1690.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
        n2 = n3 = n5 = 0
        for i in range(n - 1):
            while ugly[n2] * 2 <= ugly[i]:
                n2 += 1
            while ugly[n3] * 3 <= ugly[i]:
                n3 += 1
            while ugly[n5] * 5 <= ugly[i]:
                n5 += 1
            ugly[i + 1] = min(ugly[n2] * 2, ugly[n3] * 3, ugly[n5] * 5)
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.nthUglyNumber(10) == 12)
