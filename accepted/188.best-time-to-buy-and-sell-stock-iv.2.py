#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv
#
# Hard (24.17%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2\n[]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        if k > n // 2:
            return self.quick(prices)

        dp = [0] * n
        for i in range(1, k + 1):
            buy = -prices[0]
            preprofit = 0
            for j in range(1, n):
                temp = dp[j]
                dp[j] = max(dp[j - 1], buy + prices[j])
                buy = max(buy, preprofit - prices[j])
                preprofit = temp
        return dp[-1]

    def quick(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    sol = Solution()
    assert(sol.maxProfit(2, [7, 1, 5, 3, 6, 4]) == 7)
