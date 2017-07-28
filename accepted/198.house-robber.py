#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber
#
# Easy (38.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases. Also thanks to @ts for adding additional test cases.
#


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preTwo, preOne = 0, 0
        for num in nums:
            preTwo, preOne = preOne, max(preOne, preTwo + num)
        return preOne


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 5, 7, 3]
    print(sol.rob(arr))
