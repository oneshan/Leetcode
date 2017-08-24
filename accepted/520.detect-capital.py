#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital
#
# Easy (52.20%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"USA"'
#
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
#
#
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter,
# like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
#
# Example 1:
#
# Input: "USA"
# Output: True
#
#
#
# Example 2:
#
# Input: "FlaG"
# Output: False
#
#
#
# Note:
# The input will be a non-empty word consisting of uppercase and lowercase
# latin letters.
#
#


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True

        preUpper = word[0] < 'a'
        allUpper = preUpper and word[1] < 'a'
        for ch in word:
            if ch < 'a' and not preUpper:
                return False
            elif ch >= 'a' and allUpper:
                return False
            preUpper = ch < 'a'

        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.detectCapitalUse("USA") is True)
    assert(sol.detectCapitalUse("test") is True)
    assert(sol.detectCapitalUse("Leetcode") is True)
    assert(sol.detectCapitalUse("FlaG") is False)
    assert(sol.detectCapitalUse("AAAa") is False)
    assert(sol.detectCapitalUse("mL") is False)
