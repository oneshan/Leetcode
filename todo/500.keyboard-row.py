#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row
#
# Easy (60.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below. 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# Note:
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
