#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements
#
# Medium (47.64%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#
# Note: 
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#
#
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1

        ans = []
        for key in table:
            if k > 0:
                heapq.heappush(ans, (table[key], key))
                k -= 1
            elif table[key] > ans[0][0]:
                heapq.heappush(ans, (table[key], key))
                heapq.heappop(ans)

        return [key for freq, key in ans[::-1]]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2])
