#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence
#
# Medium (38.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,4,5]'
#
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
#
#
# Formally the function should:
# Return true if there exists i, j, k  
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 
# else return false.
#
#
#
# Your algorithm should run in O(n) time complexity and O(1) space
# complexity.
#
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
#
# Given [5, 4, 3, 2, 1],
# return false.
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and
# creating all test cases.
#
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n1 = n2 = float('inf')
        for num in nums:
            if num <= n1:
                n1 = num
            elif num <= n2:
                n2 = num
            else:
                return True
        return False
