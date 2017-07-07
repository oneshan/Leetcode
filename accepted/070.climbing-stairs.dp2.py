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
        preOne, preTwo = 1, 1
        for i in range(1, n):
            preTwo, preOne = preOne, preOne + preTwo

        return preOne

if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(1))
    print(sol.climbStairs(2))
    print(sol.climbStairs(10))
