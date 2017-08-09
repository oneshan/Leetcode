#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change
#
# Medium (26.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n0'
#
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
#
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
#
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        queue = [0]
        count = 0
        visited = {}
        while queue:
            size = len(queue)
            for _ in range(size):
                value = queue.pop(0)
                if value == amount:
                    return count
                for coin in coins:
                    next_value = coin + value
                    if next_value in visited:
                        continue
                    if next_value > amount:
                        continue
                    visited[next_value] = None
                    queue.append(next_value)
            count += 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert(sol.coinChange([1, 2, 5], 11) == 3)
    assert(sol.coinChange([2], 3) == -1)
    assert(sol.coinChange([2], 0) == 0)
