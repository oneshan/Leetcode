#
# [532] K-diff Pairs in an Array
#
# https://leetcode.com/problems/k-diff-pairs-in-an-array
#
# Easy (27.99%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,1,4,1,5]\n2'
#
#
# Given an array of integers and an integer k, you need to find the number of
# unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
# pair (i, j), where i and j are both numbers in the array and their absolute
# difference is k.
#
#
#
# Example 1:
#
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3,
# 5).Although we have two 1s in the input, we should only return the number of
# unique pairs.
#
#
#
# Example 2:
#
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
# and (4, 5).
#
#
#
# Example 3:
#
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).
#
#
#
# Note:
#
# The pairs (i, j) and (j, i) count as the same pair.
# The length of the array won't exceed 10,000.
# All the integers in the given input belong to the range: [-1e7, 1e7].
#
#
#


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        ans = 0
        nums.sort()

        i, j, n = 0, 1, len(nums)
        while j < n:
            if i == j or nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                ans += 1
                i += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1
                j = max(j, i + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findPairs([1, 3, 1, 5, 4], 0) == 1)
    assert(sol.findPairs([1, 2, 3, 4, 5], 1) == 4)
    assert(sol.findPairs([3, 1, 4, 1, 5], 2) == 2)
