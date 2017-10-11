#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings
#
# Medium (56.20%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abc"'
#
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
#
#
#
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters. 
#
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
# Note:
#
# The input string length won't exceed 1000.
#
#
#


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for i in range(len(s)):
            self.recur(s, i, i)
            self.recur(s, i, i + 1)
        return self.count

    def recur(self, s, start, end):
        while start >= 0 and end < len(s):
            if s[start] != s[end]:
                break
            start -= 1
            end += 1
        self.count += (end - start) // 2


if __name__ == "__main__":
    sol = Solution()
    assert(sol.countSubstrings("abc") == 3)
    assert(sol.countSubstrings("aaa") == 6)
