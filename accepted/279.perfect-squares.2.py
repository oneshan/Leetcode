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

        if n & 7 == 7:
            return 4

        square = []
        i = 1
        while i * i <= n:
            square.append(i * i)
            i += 1

        if n in square:
            return 1

        p1, p2 = 0, len(square) - 1
        while p1 <= p2:
            if square[p1] + square[p2] == n:
                return 2
            elif square[p1] + square[p2] > n:
                p2 -= 1
            else:
                p1 += 1
        return 3


if __name__ == "__main__":
    sol = Solution()
    assert(sol.numSquares(1) == 1)
    assert(sol.numSquares(2) == 2)
    assert(sol.numSquares(12) == 3)
    assert(sol.numSquares(13) == 2)
