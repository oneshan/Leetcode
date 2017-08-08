#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern
#
# Easy (32.83%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# ⁠Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Examples:
#
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
#
#
#
#
# Notes:
# You may assume pattern contains only owercase letters, and str contains
# lowercase letters separated by a single space.
#
#
# Credits:Special thanks to @minglotus6 for adding this problem and creating
# all test cases.
#


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False

        p2w, w2p = {}, {}
        for i in range(len(pattern)):
            if pattern[i] in p2w and p2w[pattern[i]] != words[i]:
                return False
            if words[i] in w2p and w2p[words[i]] != pattern[i]:
                return False
            p2w[pattern[i]] = words[i]
            w2p[words[i]] = pattern[i]

        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.wordPattern("abba", "dog cat cat dog") is True)
    assert(sol.wordPattern("abba", "dog cat cat fish") is False)
    assert(sol.wordPattern("aaaa", "dog cat cat dog") is False)
    assert(sol.wordPattern("abba", "dog dog dog dog") is False)
