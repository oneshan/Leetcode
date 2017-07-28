#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands
#
# Medium (34.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["11110","11010","11000","00000"]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
# 11110110101100000000
# Answer: 1
# Example 2:
# 11000110000010000011
# Answer: 3
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        grid = [list(grid[i]) for i in range(m)]
        ans = 0

        def DFS(x, y):
            grid[x][y] = '0'
            if x < m - 1 and grid[x + 1][y] == '1':
                DFS(x + 1, y)
            if x > 0 and grid[x - 1][y] == '1':
                DFS(x - 1, y)
            if y < n - 1 and grid[x][y + 1] == '1':
                DFS(x, y + 1)
            if y > 0 and grid[x][y - 1] == '1':
                DFS(x, y - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                DFS(i, j)
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [
        "11110",
        "11010",
        "11000",
        "00000"
    ]
    print(sol.numIslands(arr))
    arr = [
        "11000",
        "11000",
        "00100",
        "00011"
    ]
    print(sol.numIslands(arr))
    arr = ["010", "101", "010"]
    print(sol.numIslands(arr))
