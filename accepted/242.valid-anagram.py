#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram
#
# Easy (46.08%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""'
#
# Given two strings s and t, write a function to determine if t is an anagram
# of s. 
# 
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
# 
# 
# Note:
# You may assume the string contains only lowercase alphabets.
# 
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your
# solution to such case?
#


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        table = {}
        for ch in s:
            table[ch] = table.get(ch, 0) + 1
        for ch in t:
            table[ch] = table.get(ch, 0) - 1
            if table[ch] < 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isAnagram("rar", "car") is False)
    assert(sol.isAnagram("anagram", "naagram") is True)
