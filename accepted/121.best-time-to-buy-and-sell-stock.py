#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
#
# Easy (40.73%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Example 1:
#
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
# than buying price)
#
#
#
# Example 2:
#
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curr_min, max_profit = float('inf'), 0
        for price in prices:
            curr_min = min(curr_min, price)
            max_profit = max(max_profit, price - curr_min)
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
