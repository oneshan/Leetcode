#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix
#
# Medium (32.92%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1: 
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2: 
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#
#


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])
        ans = [[0] * c for _ in range(r)]
        queue = [(x, y) for x in range(r) for y in range(c) if matrix[x][y]]

        step = 0
        while queue:
            step += 1
            new_queue = []
            for x, y in queue:
                for (dx, dy) in (1, 0), (0, 1), (-1, 0), (0, -1):
                    if 0 <= x + dx < r and 0 <= y + dy < c:
                        if not matrix[x + dx][y + dy] or 0 < ans[x + dx][y + dy] < step:
                            ans[x][y] = step
                if not ans[x][y]:
                    new_queue.append((x, y))
            queue = new_queue

        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [
        [0, 0, 0],
        [0, 1, 0],
        [1, 1, 1]
    ]
    print(sol.updateMatrix(arr))
