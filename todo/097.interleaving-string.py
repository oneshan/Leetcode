#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string
#
# Hard (24.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""\n""'
#
# 
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# 
# 
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
# 
# 
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
# 
#
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
