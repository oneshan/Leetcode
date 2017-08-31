#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i
#
# Easy (38.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# Note:
# 
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
#


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = 0
        for i in range(k):
            total += nums[i]

        ans = total
        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            ans = max(ans, total)
        return ans * 1.0 / k


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75)
    assert(sol.findMaxAverage([5], 1) == 5)
