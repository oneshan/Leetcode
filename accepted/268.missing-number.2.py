#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number
#
# Easy (44.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for idx, elem in enumerate(nums, 1):
            ans ^= idx
            ans ^= elem
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert(sol.missingNumber([0, 1, 3]) == 2)
