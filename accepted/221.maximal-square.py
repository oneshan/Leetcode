#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square
#
# Medium (28.42%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["10100","10111","11111","10010"]'
#
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Return 4.
#
#
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxLen = 0

        for x in range(m):
            dp[x][0] = 1 if matrix[x][0] == '1' else 0
            maxLen = max(maxLen, dp[x][0])

        for y in range(n):
            dp[0][y] = 1 if matrix[0][y] == '1' else 0
            maxLen = max(maxLen, dp[0][y])

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][y] == '0':
                    continue
                dp[x][y] = min(dp[x - 1][y],
                               dp[x][y - 1],
                               dp[x - 1][y - 1]) + 1
                maxLen = max(maxLen, dp[x][y])

        return maxLen * maxLen


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        "10100",
        "10111",
        "11111",
        "10010",
    ]
    assert(sol.maximalSquare(matrix) == 4)

    matrix = [
        "00",
        "00",
    ]
    assert(sol.maximalSquare(matrix) == 0)

    matrix = [
        "1111",
        "1111",
        "1111",
    ]
    assert(sol.maximalSquare(matrix) == 9)
