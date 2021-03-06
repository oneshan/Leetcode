#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum
#
# Medium (43.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1,1,1,1]\n3'
#
#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
#
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
#
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#
#
# Note:
#
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#
#
#


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = {0: 1}
        for num in nums:
            temp = {}
            for i in dp.keys():
                temp[i + num] = temp.get(i + num, 0) + dp[i]
                temp[i - num] = temp.get(i - num, 0) + dp[i]
            dp = temp
        return dp.get(S, 0)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5)
