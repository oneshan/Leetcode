# -*- coding: utf8 -*-
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons
#
# Hard (42.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,1,5,8]'
#
#
# ⁠   Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# ⁠   number on it represented by array nums.
#
# ⁠   You are asked to burst all the balloons. If the you burst
# ⁠   balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
# left
# ⁠   and right are adjacent indices of i. After the burst, the left and right
# ⁠   then becomes adjacent.
#
#
# ⁠   Find the maximum coins you can collect by bursting the balloons wisely.
#
#
# ⁠   Note: 
# ⁠   (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore
# you can not burst them.
# ⁠   (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
#
#
# ⁠   Example:
#
#
# ⁠   Given [3, 1, 5, 8]
#
#
# ⁠   Return 167
#
#
# ⁠   nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# ⁠  coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def recur(i, j):
            if dp[i][j]:
                return dp[i][j]
            for k in range(i, j + 1):
                dp[i][j] = max(
                    dp[i][j],
                    recur(i, k - 1) + nums[i - 1] * nums[k] * nums[j + 1] + recur(k + 1, j)
                )
            return dp[i][j]

        recur(1, n - 2)
        return dp[1][-2]

if __name__ == "__main__":
    sol = Solution()
    arr = [3, 1, 5, 8]
    assert(sol.maxCoins(arr) == 167)
