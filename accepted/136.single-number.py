#
# [136] Single Number
#
# https://leetcode.com/problems/single-number
#
# Easy (54.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given an array of integers, every element appears twice except for one. Find
# that single one.
#
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1]
    print(sol.singleNumber(arr))
    arr = [1, 2, 2, 3, 1]
    print(sol.singleNumber(arr))
