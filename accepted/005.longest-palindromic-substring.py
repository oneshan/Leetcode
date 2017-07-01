#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring
#
# Medium (25.13%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
#
#
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxLen, self.ans = 0, ""

        def find(left, right):
            while 0 <= left and right < len(s):
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if self.maxLen < right - left - 1:
                self.ans, self.maxLen = s[left + 1: right], right - left - 1

        for i in range(len(s)):
            find(i, i)      # Odd case
            find(i, i + 1)  # Even case
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babab"))
    print(sol.longestPalindrome("cbbd"))
    print(sol.longestPalindrome("baaaab"))
    print(sol.longestPalindrome("baaab"))
    print(sol.longestPalindrome("baab"))
    print(sol.longestPalindrome("a"))
    print(sol.longestPalindrome(""))
