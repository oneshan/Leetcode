#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern
#
# Easy (38.17%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together.  You may
# assume the given string consists of lowercase English letters only and its
# length  will not exceed 10000.
#
# Example 1:
#
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
#
#
#
# Example 2:
#
# Input: "aba"
#
# Output: False
#
#
#
# Example 3:
#
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
#
#
#


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, (n >> 1) + 1):
            if n % i:
                continue
            j, substr = i, s[:i]
            while j < n:
                if s[j:j + i] != substr:
                    break
                j += i
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.repeatedSubstringPattern("abab") is True)
    assert(sol.repeatedSubstringPattern("aba") is False)
    assert(sol.repeatedSubstringPattern("abcabcabcabc") is True)
