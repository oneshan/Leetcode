#
# [256] Paint House
#
# https://leetcode.com/problems/paint-house
#
# algorithms
# Easy (46.11%)
# Total Accepted:    27.7K
# Total Submissions: 60.1K
# Testcase Example:  '[]'
#
#
# There are a row of n houses, each house can be painted with one of the three
# colors: red, blue or green. The cost of painting each house with a certain
# color is different. You have to paint all the houses such that no two
# adjacent houses have the same color.
#
#
# The cost of painting each house with a certain color is represented by a n x
# 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color red; costs[1][2] is the cost of painting house 1 with color green, and
# so on... Find the minimum cost to paint all houses.
#
#
# Note:
# All costs are positive integers.
#


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        dp = [0, 0, 0]
        for cost in costs:
            nxt = [
                cost[0] + min(dp[1], dp[2]),
                cost[1] + min(dp[0], dp[2]),
                cost[2] + min(dp[0], dp[1])
            ]
            dp = nxt
        return min(dp)

if __name__ == "__main__":
    sol = Solution()
    arr = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
    assert(sol.minCost(arr) == 10)
