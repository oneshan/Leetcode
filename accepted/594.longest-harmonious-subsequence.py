#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence
#
# Easy (39.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmonious array is an array where the difference between its
# maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
#
# Example 1:
#
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
#
# Note:
# The length of the input array will not exceed 20,000.
#
#
#
#


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = {}
        count = 0
        for num in nums:
            table[num] = table.get(num, 0) + 1
        for num in table:
            if num + 1 in table:
                count = max(count, table[num] + table[num + 1])
        return count


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5)
