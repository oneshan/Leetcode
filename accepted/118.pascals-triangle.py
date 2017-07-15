#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle
#
# Easy (38.12%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
#
# For example, given numRows = 5,
# Return
#
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []

        ans = [[1]]
        for i in range(1, numRows):
            ans += [1] + [ans[-1][j] + ans[-1][j - 1] for j in range(1, i)] + [1],
        return ans


if __name__ == "__main__":
    sol = Solution()
    for i in range(6):
        print(i, sol.generate(i))
