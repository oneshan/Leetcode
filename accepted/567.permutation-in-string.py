#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string
#
# Medium (36.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
#
# Example 1:
#
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
#
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
#
# Note:
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
#
#
#


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        target = [0] * 26
        for ch in s1:
            target[ord(ch) - 97] += 1

        window = [0] * 26
        for idx, ch in enumerate(s2):
            window[ord(ch) - 97] += 1
            if idx >= n:
                window[ord(s2[idx - n]) - 97] -= 1
            if window == target:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.checkInclusion("ab", "eidbaooo") is True)
    assert(sol.checkInclusion("ab", "eidboaoo") is False)
