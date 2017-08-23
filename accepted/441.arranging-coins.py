#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins
#
# Easy (36.28%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
#
#
#
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
#
#
#


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            total = (mid + 1) * mid // 2
            if n == total:
                return mid
            elif n < total:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    sol = Solution()
    assert(sol.arrangeCoins(5) == 2)
    assert(sol.arrangeCoins(8) == 3)
