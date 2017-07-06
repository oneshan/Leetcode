#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix
#
# Medium (25.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
#
#
# For example,
# Given the following matrix:
#
#
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
#
#
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        M = len(matrix)
        N = len(matrix[0])

        ans = []

        row_s, row_e, col_s, col_e = 0, M - 1, 0, N - 1
        while row_s <= row_e and col_s <= col_e:

            for j in range(col_s, col_e + 1):
                ans += matrix[row_s][j],
            row_s += 1

            for i in range(row_s, row_e + 1):
                ans += matrix[i][col_e],
            col_e -= 1

            if row_s <= row_e:
                for j in range(col_e, col_s - 1, -1):
                    ans += matrix[row_e][j],
                row_e -= 1

            if col_s <= col_e:
                for i in range(row_e, row_s - 1, -1):
                    ans += matrix[i][col_s],
                col_s += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.spiralOrder(matrix))

    matrix = [[2, 3]]
    print(sol.spiralOrder(matrix))
