#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum
#
# Medium (38.16%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[0]]
    print(sol.minPathSum(grid))

    grid = [[1, 3, 5], [2, 4, 8], [6, 7, 9]]
    print(sol.minPathSum(grid))
