#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array
#
# algorithms
# Easy (46.72%)
# Total Accepted:    9.7K
# Total Submissions: 20.7K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
#
# Example 1:
#
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
#
#
#
#
# Example 2:
#
# Input: [1,2,2,3,1,4,2]
# Output: 6
#
#
#
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
#
#
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = defaultdict(list)
        count = defaultdict(int)
        for idx, num in enumerate(nums):
            count[num] += 1
            table[num].append(idx)
        maxDegree = max(count.values())

        minLen = float('inf')
        for num in count:
            if count[num] == maxDegree:
                minLen = min(minLen, table[num][-1] - table[num][0] + 1)
        return minLen


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findShortestSubArray([1, 2, 2, 3, 1]) == 2)
    assert(sol.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6)
