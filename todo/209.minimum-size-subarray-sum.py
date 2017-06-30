#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum
#
# Medium (30.21%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
# 
# 
# click to show more practice.
# 
# More practice:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n).
# 
# 
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
