#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii
#
# Medium (38.28%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
#
#
#
#
# For example,
#
# Consider the following matrix:
#
#
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
#
#
# Given target = 5, return true.
# Given target = 20, return false.
#


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] > target:
                break
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert(sol.searchMatrix(matrix, 5) is True)
    assert(sol.searchMatrix(matrix, 21) is True)
    assert(sol.searchMatrix(matrix, 20) is False)
