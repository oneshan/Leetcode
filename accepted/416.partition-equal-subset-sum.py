#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum
#
# Medium (38.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = 0
        for num in nums:
            total += num

        if total & 1:
            return False

        target = total // 2
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for num in nums:
            if num == target:
                return True
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]

        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.canPartition([1, 5, 11, 5]) is True)
    assert(sol.canPartition([1, 2, 3, 5]) is False)
    assert(sol.canPartition([1, 2, 5]) is False)
    assert(sol.canPartition([3, 3, 3, 4, 5]) is True)
