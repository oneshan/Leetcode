#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii
#
# Medium (31.50%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0]]'
#
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
# ⁠ [0,0,0],
# ⁠ [0,1,0],
# ⁠ [0,0,0]
# ]
#
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.
#


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            dp[i][0] = 0 if obstacleGrid[i][0] else dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = 0 if obstacleGrid[0][j] else dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    print(sol.uniquePathsWithObstacles(matrix))

    matrix = [[1]]
    print(sol.uniquePathsWithObstacles(matrix))
