#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii
#
# Hard (29.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        profit = [0] * n

        minV, maxV = float('inf'), float('-inf')
        max_profit_l, max_profit_r = 0, 0
        for i in range(n):
            minV = min(minV, prices[i])
            max_profit_l = max(max_profit_l, prices[i] - minV)
            profit[i] += max_profit_l

            maxV = max(maxV, prices[-1 - i])
            max_profit_r = max(max_profit_r, maxV - prices[-1 - i])
            profit[-1 - i] += max_profit_r

        return max(profit)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 5, 3, 6, 1, 7]))
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
