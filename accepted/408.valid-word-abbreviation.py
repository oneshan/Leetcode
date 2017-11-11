#
# [408] Valid Word Abbreviation
#
# https://leetcode.com/problems/valid-word-abbreviation
#
# algorithms
# Easy (28.14%)
# Total Accepted:    12.7K
# Total Submissions: 45.2K
# Testcase Example:  '"internationalization"\n"i12iz4n"'
#
#
# Given a non-empty string s and an abbreviation abbr, return whether the
# string matches with the given abbreviation.
#
#
# A string such as "word" contains only the following valid abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
#
# Notice that only the above abbreviations are valid abbreviations of the
# string "word". Any other string is not a valid abbreviation of "word".
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase
# letters and digits.
#
#
# Example 1:
#
# Given s = "internationalization", abbr = "i12iz4n":
#
# Return true.
#
#
#
# Example 2:
#
# Given s = "apple", abbr = "a2e":
#
# Return false.
#
#
#
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        wlen, alen = len(word), len(abbr)
        i = j = 0
        while True:
            num = ""
            while i < alen and abbr[i] in '0123456789':
                num += abbr[i]
                i += 1
            if num:
                if num[0] == '0':
                    return False
                j += int(num)
                num = ""
            if i == alen:
                return j == wlen
            if j >= wlen or word[j] != abbr[i]:
                return False
            i += 1
            j += 1

if __name__ == "__main__":
    sol = Solution()
    assert(sol.validWordAbbreviation("internationalization", "i12iz4n") is True)
    assert(sol.validWordAbbreviation("apple", "a2e") is False)
    assert(sol.validWordAbbreviation("a", "01") is False)
