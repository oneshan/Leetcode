#
# [120] Triangle
#
# https://leetcode.com/problems/triangle
#
# Medium (33.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[-10]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
#
# For example, given the following triangle
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
#
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        n = len(triangle)
        arr = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                arr[j] = triangle[i][j] + min(arr[j], arr[j + 1])
        return arr[0]


if __name__ == "__main__":
    sol = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(sol.minimumTotal(triangle))
