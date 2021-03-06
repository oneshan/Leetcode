#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string
#
# Medium (15.71%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
#
# Given an input string, reverse the string word by word.
#
#
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
#
#
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.
#
#
# click to show clarification.
#
# Clarification:
#
#
#
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing
# spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
#
#
#
#


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Solve by built-in function
        # return ' '.join(s.split()[::-1])
        ans = word = ""
        for ch in s:
            if ch != ' ':
                word += ch
            elif word:
                ans = word + ' ' + ans
                word = ''

        if word:
            ans = word + ' ' + ans
        return ans[:-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.reverseWords("the sky is blue") == "blue is sky the")
