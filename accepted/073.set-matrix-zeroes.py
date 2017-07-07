#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes
#
# Medium (35.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0]]'
#
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in place.
#
#
# click to show follow up.
#
# Follow up:
#
#
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
#


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])

        first_col = any(0 == matrix[i][0] for i in range(M))
        first_row = any(0 == matrix[0][j] for j in range(N))

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(1, N):
                    matrix[i][j] = 0

        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(1, M):
                    matrix[i][j] = 0

        if first_col:
            for i in range(M):
                matrix[i][0] = 0

        if first_row:
            for j in range(N):
                matrix[0][j] = 0

        for i in range(M):
            print(matrix[i])


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 1, 1]
    ]
    sol.setZeroes(matrix)
