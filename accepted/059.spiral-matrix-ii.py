#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii
#
# Medium (39.20%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given an integer n, generate a square matrix filled with elements from 1 to
# n2 in spiral order.
#
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
#
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]

        count = 1
        row_s, row_e, col_s, col_e = 0, n - 1, 0, n - 1
        while row_s <= row_e and col_s <= col_e:

            for j in range(col_s, col_e + 1):
                ans[row_s][j] = count
                count += 1
            row_s += 1

            for i in range(row_s, row_e + 1):
                ans[i][col_e] = count
                count += 1
            col_e -= 1

            if row_s <= row_e:
                for j in range(col_e, col_s - 1, -1):
                    ans[row_e][j] = count
                    count += 1
                row_e -= 1

            if col_s <= col_e:
                for i in range(row_e, row_s - 1, -1):
                    ans[i][col_s] = count
                    count += 1
                col_s += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateMatrix(4))
