#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii
#
# Medium (41.15%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
#
# Given an array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
#
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
        one = two = three = 0
        for num in nums:
            two |= one & num
            one ^= num
            three = one & two
            two ^= three
            one ^= three
        return one

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2, 2, 3, 1, 1, 4, 4, 4]
    print(sol.singleNumber(arr))
