#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs
#
# Easy (39.67%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Note: Given n will be a positive integer.
#
#


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(10))
