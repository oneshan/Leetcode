#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image
#
# Medium (38.21%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1]]'
#
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Follow up:
# Could you do this in-place?


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Flip anti diagonal
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[-1 - j][-1 - i] = matrix[-1 - j][-1 - i], matrix[i][j]

        # Flip vertical
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[-1 - i][j] = matrix[-1 - i][j], matrix[i][j]


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol.rotate(matrix)
