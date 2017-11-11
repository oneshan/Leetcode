# -*- coding: utf8 -*-
#
# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy
#
# algorithms
# Medium (39.15%)
# Total Accepted:    18.6K
# Total Submissions: 47.5K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# ⁠Note that you can only put the bomb at an empty cell. 
#
# Example:
#
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
#
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        ans = rowcnt = 0
        colcnt = [0] * n
        for i in range(m):
            for j in range(n):
                if j == 0 or grid[i][j - 1] == 'W':
                    rowcnt = 0
                    for k in range(j, n):
                        if grid[i][k] == 'W':
                            break
                        rowcnt += grid[i][k] == 'E'

                if i == 0 or grid[i - 1][j] == 'W':
                    colcnt[j] = 0
                    for k in range(i, m):
                        if grid[k][j] == 'W':
                            break
                        colcnt[j] += grid[k][j] == 'E'

                if grid[i][j] == '0':
                    ans = max(ans, rowcnt + colcnt[j])
        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        ['0', 'E', '0', '0'],
        ['E', '0', 'W', 'E'],
        ['0', 'E', '0', '0'],
    ]
    assert(sol.maxKilledEnemies(matrix) == 3)
