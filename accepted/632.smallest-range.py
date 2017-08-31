#
# [632] Smallest Range
#
# https://leetcode.com/problems/smallest-range
#
# Hard (42.77%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists. 
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
#
# Example 1:
#
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
#
#
# Note:
#
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# ⁠-105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to
# List<List<Integer>>. And after you reset the code template, you'll see this
# point.
#
#
#
#
import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        minheap = []
        k = len(nums)
        for i in range(k):
            heapq.heappush(minheap, (nums[i][0], i, 0))

        _max = max(minheap)[0]
        ans = (float('inf'), 0, 0)

        while True:
            val, list_i, idx = heapq.heappop(minheap)
            if ans[0] > _max - val:
                ans = (_max - val, val, _max)

            idx += 1
            if idx == len(nums[list_i]):
                break

            heapq.heappush(minheap, (nums[list_i][idx], list_i, idx))
            _max = max(_max, nums[list_i][idx])

        return [ans[1], ans[2]]


if __name__ == "__main__":
    sol = Solution()
    nums = [
        [4, 10, 15, 24, 26],
        [0, 9, 12, 20],
        [5, 18, 22, 30]
    ]
    assert(sol.smallestRange(nums) == [20, 24])
