#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence
#
# Hard (36.42%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[100,4,200,1,3,2]'
#
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
# 4.
#
#
# Your algorithm should run in O(n) complexity.
#
#


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        union = {num: num for num in nums}
        max_length = 0

        for key in union:
            if union[key] != key:
                continue

            length, y = 1, key + 1
            while y in union:
                union[y] = key
                y += 1
                length += 1

            max_length = max(max_length, length)

        return max_length


if __name__ == "__main__":
    sol = Solution()
    arr = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(arr))
