#
# [266] Palindrome Permutation
#
# https://leetcode.com/problems/palindrome-permutation
#
# algorithms
# Easy (57.37%)
# Total Accepted:    37K
# Total Submissions: 64.5K
# Testcase Example:  '"aab"'
#
# Given a string, determine if a permutation of the string could form a
# palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#
#
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = 0
        for ch in s:
            num ^= (1 << ord(ch))
        return num == 0 or (num & (num - 1) == 0)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.canPermutePalindrome("code") is False)
    assert(sol.canPermutePalindrome("carerac") is True)
