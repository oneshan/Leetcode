#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv
#
# Medium (41.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]\n4'
#
# ⁠Given an integer array with all positive numbers and no duplicates, find the
# number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
#
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers? 
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i < num:
                    break
                dp[i] += dp[i - num]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.combinationSum4([1, 2, 3], 4) == 7)
