#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii
#
# algorithms
# Hard (39.18%)
# Total Accepted:    26.5K
# Total Submissions: 67.7K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water.
# We may perform an addLand operation which turns the water at position (row,
# col) into a land.
# Given a list of positions to operate, count the number of islands after each
# addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example:
# Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
#
# 0 0 0
# 0 0 0
# 0 0 0
#
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
#
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
#
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
#
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
#
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
#
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
#
# We return the result as an array: [1, 1, 2, 3]
#
# Challenge:
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
#


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not m or not n:
            return []

        def getroot(i, parents):
            while i != parents[i]:
                parents[i] = parents[parents[i]]
                i = parents[i]
            return i

        parents = {}
        count = 0
        ans = []
        for pos in positions:
            i = pos[0] * n + pos[1]
            parents[i] = i
            count += 1

            for way in (0, 1), (1, 0), (-1, 0), (0, -1):
                x, y = pos[0] + way[0], pos[1] + way[1]
                j = x * n + y
                if 0 <= x < m and 0 <= y < n and j in parents:
                    root = getroot(j, parents)
                    if root != i:
                        parents[root] = i
                        count -= 1

            ans.append(count)

        return ans


if __name__ == "__main__":
    sol = Solution()
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    assert(sol.numIslands2(3, 3, positions) == [1, 1, 2, 3])
