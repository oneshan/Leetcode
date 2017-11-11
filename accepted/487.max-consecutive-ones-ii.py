# -*- coding: utf8 -*-
#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii
#
# algorithms
# Medium (45.53%)
# Total Accepted:    8.6K
# Total Submissions: 18.9K
# Testcase Example:  '[1,0,1,1,0,1]'
#
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
#
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
#
#


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = prev = curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                ans = max(ans, prev + curr + 1)
                prev, curr = curr, 0
        ans = max(ans, prev + curr + 1)
        return min(len(nums), ans)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.findMaxConsecutiveOnes([1, 1]) == 2)
    assert(sol.findMaxConsecutiveOnes([0]) == 1)
    assert(sol.findMaxConsecutiveOnes([1]) == 1)
    assert(sol.findMaxConsecutiveOnes([1, 1, 0, 1]) == 4)
    assert(sol.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 4)
