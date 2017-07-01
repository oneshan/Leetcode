#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# Easy (33.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return [table[num], idx]
            table[target - num] = idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([1, 2, 3], 4))
    print(sol.twoSum([2, 7, 11, 15], 9))
