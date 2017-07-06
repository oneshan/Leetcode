#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray
#
# Easy (39.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
#
# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
#
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
#
# click to show more practice.
#
# More practice:
#
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
#
#


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        maxSum, currSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if currSum < 0:
                currSum = 0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum


if __name__ == "__main__":
    sol = Solution()
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(arr))
