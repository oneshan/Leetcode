#
# [392] Is Subsequence
#
# https://leetcode.com/problems/is-subsequence
#
# Medium (44.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abc"\n"ahbgdc"'
#
#
# Given a string s and a string t, check if s is subsequence of t.
#
#
#
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long (length ~= 500,000) string, and s is a short
# string (<=100).
#
#
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ace" is a
# subsequence of "abcde" while "aec" is not).
#
#
# Example 1:
# s = "abc", t = "ahbgdc"
#
#
# Return true.
#
#
# Example 2:
# s = "axc", t = "ahbgdc"
#
#
# Return false.
#
#
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you
# want to check one by one to see if T has its subsequence. In this scenario,
# how would you change your code?
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
from bisect import bisect_left


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = {}
        for idx, ch in enumerate(t):
            table.setdefault(ch, [])
            table[ch].append(idx)

        last = 0
        for ch in s:
            if ch not in table:
                return False
            idx = bisect_left(table[ch], last)
            if idx == len(table[ch]):
                return False
            last = table[ch][idx] + 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert(sol.isSubsequence("adc", "ahbgdc") is True)
