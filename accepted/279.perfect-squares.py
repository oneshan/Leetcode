#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares
#
# Medium (36.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
#
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while not (n & 3):
            n >>= 2

        square = []
        i = 1
        while i * i <= n:
            square.append(i * i)
            i += 1

        dp = [4] * (n + 1)
        for i in square:
            dp[i] = 1
            for j in range(n + 1 - i):
                dp[i + j] = min(dp[i + j], dp[j] + 1)

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.numSquares(12) == 3)
    assert(sol.numSquares(13) == 2)
