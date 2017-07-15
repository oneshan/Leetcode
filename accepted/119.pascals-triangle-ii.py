#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii
#
# Easy (36.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given an index k, return the kth row of the Pascal's triangle.
#
#
# For example, given k = 3,
# Return [1,3,3,1].
#
#
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            ans[1:i] = [ans[j - 1] + ans[j] for j in range(1, i)]
        return ans


if __name__ == "__main__":
    sol = Solution()
    for i in range(6):
        print(i, sol.getRow(i))
