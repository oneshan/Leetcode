#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range
#
# Medium (33.78%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0\n0'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
#
#
# For example, given the range [5, 7], you should return 4.
#
#
# Credits:Special thanks to @amrsaqr for adding this problem and creating all
# test cases.
#


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m and n:
            if m == n:
                break
            m >>= 1
            n >>= 1
            i += 1
        return m << i


if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeBitwiseAnd(5, 7))
    print(sol.rangeBitwiseAnd(10, 14))
