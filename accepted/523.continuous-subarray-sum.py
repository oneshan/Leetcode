#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum
#
# Medium (22.23%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[23,2,4,6,7]\n6'
#
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to the multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
#
#
# Example 2:
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
# Note:
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False

        if k == 0:
            for i in range(1, n):
                if nums[i] == nums[i - 1] == 0:
                    return True
            return False

        nums[0] %= k
        for i in range(1, n):
            nums[i] = (nums[i] + nums[i - 1]) % k
            if nums[i] == 0:
                return True

        table = {}
        for idx, num in enumerate(nums):
            if num in table:
                return True
            table[num] = idx
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.checkSubarraySum([23, 2, 4, 6, 7], 6) is True)
    assert(sol.checkSubarraySum([23, 2, 4, 6, 7], 0) is False)
    assert(sol.checkSubarraySum([0, 0], -1) is True)
    assert(sol.checkSubarraySum([0, 0], 0) is True)
    assert(sol.checkSubarraySum([1, 1], 2) is True)
