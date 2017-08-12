#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number
#
# Medium (22.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Key(str):
    def __lt__(a, b):
        return a + b < b + a


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=Key, reverse=True)
        return "".join(nums).lstrip("0") or "0"


if __name__ == "__main__":
    sol = Solution()
    assert(sol.largestNumber([3, 30, 34, 5, 9]) == '9534330')
    assert(sol.largestNumber([0, 0]) == '0')
