#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray
#
# Easy (30.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
#
#
#
# Note:
#
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=. 
#
#
#


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxV, minV = nums[0], nums[-1]
        p1, p2 = 1, 0
        for i in range(n):
            if maxV > nums[i]:
                p2 = i
            if minV < nums[-i - 1]:
                p1 = n - i - 1
            minV = min(minV, nums[-i - 1])
            maxV = max(maxV, nums[i])
        return (p2 - p1 + 1)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5)
