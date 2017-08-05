#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii
#
# Medium (51.05%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,1,3,2,5]'
#
#
# Given an array of numbers nums, in which exactly two elements appear only
# once and all the other elements appear exactly twice. Find the two elements
# that appear only once.
#
#
# For example:
#
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
#
# Note:
#
# The order of the result is not important. So in the above example, [5, 3] is
# also correct.
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant space complexity?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num

        mask = 1
        while not (xor & mask):
            mask <<= 1

        x = y = 0
        for num in nums:
            if num & mask:
                x ^= num
            else:
                y ^= num

        return [x, y]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.singleNumber([1, 2, 1, 3, 2, 5]) == [3, 5])
