#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words
#
# Hard (21.86%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
# 
# 
# 
# You should return the indices: [0,9].
# (order does not matter).
# 
#
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
