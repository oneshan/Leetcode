#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths
#
# Medium (40.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
#
# Note: m and n will be at most 100.


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(1, 2))
    print(sol.uniquePaths(3, 7))
