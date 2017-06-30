#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes
#
# Hard (31.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
# 
# 
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
# 
# 
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
# you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# 
#
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
