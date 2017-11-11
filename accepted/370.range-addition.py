# -*- coding: utf8 -*-
#
# [370] Range Addition
#
# https://leetcode.com/problems/range-addition
#
# algorithms
# Medium (56.42%)
# Total Accepted:    14K
# Total Submissions: 24.9K
# Testcase Example:  '5\n[[1,3,2],[2,4,3],[0,2,-2]]'
#
# Assume you have an array of length n initialized with all 0's and are given k
# update operations.
#
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which
# increments each element of subarray A[startIndex ... endIndex] (startIndex
# and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
# ⁠   length = 5,
# ⁠   updates = [
# ⁠       [1,  3,  2],
# ⁠       [2,  4,  3],
# ⁠       [0,  2, -2]
# ⁠   ]
#
# Output:
#
# ⁠   [-2, 0, 3, 5, 3]
#
#
#
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
#
#
#
# Credits:Special thanks to @vinod23 for adding this problem and creating all
# test cases.
#


class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        ans = [0] * (length + 1)
        for s, e, inc in updates:
            ans[s] += inc
            ans[e + 1] -= inc

        for i in range(1, length):
            ans[i] += ans[i-1]
        ans.pop()

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]) == [-2, 0, 3, 5, 3])
