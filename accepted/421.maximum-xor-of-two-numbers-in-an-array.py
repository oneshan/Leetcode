# -*- coding: utf8 -*-
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array
#
# Medium (44.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 231.
#
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.
#
#
#


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(31, -1, -1):
            ans <<= 1
            prefix = {num >> i for num in nums}
            ans += any(ans ^ 1 ^ p in prefix for p in prefix)
        return ans

if __name__ == "__main__":
    sol = Solution()
    arr = [3, 10, 5, 25, 2, 8]
    assert(sol.findMaximumXOR(arr) == 28)
