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
        i, n = 0, len(word)
        num = 0
        for ch in abbr:
            if ch == '0' and not num:
                return False
            elif ch in '0123456789':
                num = num * 10 + int(ch)
            else:
                i += num
                num = 0
                if i >= n or word[i] != ch:
                    return False
                i += 1
        return i + num == n

if __name__ == "__main__":
    sol = Solution()
    assert(sol.validWordAbbreviation("internationalization", "i12iz4n") is True)
    assert(sol.validWordAbbreviation("apple", "a2e") is False)
    assert(sol.validWordAbbreviation("a", "01") is False)
