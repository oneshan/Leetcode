#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
#
# Easy (46.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times). However, you may not engage in multiple transactions at the
# same time (ie, you must sell the stock before you buy again).
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        i = 0
        max_profit = 0
        for j in range(1, len(prices)):
            if prices[j - 1] > prices[j]:
                max_profit += prices[j - 1] - prices[i]
                i = j
        max_profit += prices[-1] - prices[i]
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([1, 2]))
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
