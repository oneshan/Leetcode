#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences
#
# Medium (33.84%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,3,4,5]'
#
# You are given an integer array sorted in ascending order (may contain
# duplicates), you need to split them into several subsequences, where each
# subsequences consist of at least 3 consecutive integers. Return whether you
# can make such a split.
#
# Example 1:
#
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
#
#
#
# Example 2:
#
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
#
#
#
# Example 3:
#
# Input: [1,2,3,4,4,5]
# Output: False
#
#
#
# Note:
#
# The length of the input is in range of [1, 10000]
#
#
#
import heapq


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {num: [] for num in nums}

        for num in nums:
            if table.get(num - 1):
                length = heapq.heappop(table[num - 1]) + 1
            else:
                length = 1
            heapq.heappush(table[num], length)

        for num in nums:
            if table[num] and min(table[num]) < 3:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isPossible([1, 2, 3, 3, 4, 5]) is True)
    assert(sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5]) is True)
    assert(sol.isPossible([1, 2, 3, 4, 4, 5]) is False)
