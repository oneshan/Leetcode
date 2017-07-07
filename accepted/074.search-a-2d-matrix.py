#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix
#
# Medium (35.16%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
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
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
#
#
# Given target = 3, return true.
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

        M = len(matrix)
        N = len(matrix[0])

        # Find row
        left, right = 0, M - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        i = right

        # Find column
        left, right = 0, N - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print(sol.searchMatrix(matrix, 3))
    print(sol.searchMatrix(matrix, 20))
    print(sol.searchMatrix(matrix, 23))
    print(sol.searchMatrix(matrix, 33))

    matrix = [[1]]
    print(sol.searchMatrix(matrix, 2))

    matrix = [[1], [3], [5]]
    print(sol.searchMatrix(matrix, 1))
    print(sol.searchMatrix(matrix, 3))
    print(sol.searchMatrix(matrix, 5))
