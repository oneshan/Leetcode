#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word
#
# Easy (31.69%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
#
# For example, 
# Given s = "Hello World",
# return 5.
#


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastSpace = len(s)
        for i in range(lastSpace - 1, -1, -1):
            if s[i] == ' ':
                if lastSpace != i + 1:
                    return lastSpace - i - 1
                lastSpace = i
        return lastSpace

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("Hello  Worldddd  "))
    print(sol.lengthOfLastWord("    "))
    print(sol.lengthOfLastWord("a"))
