#
# [315] Count of Smaller Numbers After Self
#
# https://leetcode.com/problems/count-of-smaller-numbers-after-self
#
# Hard (34.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,2,6,1]'
#
# 
# You are given an integer array nums and you have to return a new counts
# array.
# The counts array has the property where counts[i] is 
# the number of smaller elements to the right of nums[i].
# 
# 
# Example:
# 
# 
# Given nums = [5, 2, 6, 1]
# 
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 
# 
# 
# Return the array [2, 1, 1, 0].
# 
#
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
