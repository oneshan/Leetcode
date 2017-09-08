#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching
#
# Hard (19.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aa"\n"a"'
#
# Implement wildcard pattern matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false
#
#


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p1 = p2 = 0
        last_p1 = last_p2 = -1
        while p1 < len(s):
            if p2 < len(p) and (s[p1] == p[p2] or p[p2] == '?'):
                p1 += 1
                p2 += 1
            elif p2 < len(p) and p[p2] == '*':
                p2 += 1
                last_p1, last_p2 = p1, p2
            elif last_p2 != -1:
                last_p1 += 1
                p1, p2 = last_p1, last_p2
            else:
                return False

        while p2 < len(p) and p[p2] == '*':
            p2 += 1

        return p2 == len(p)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isMatch("aa", "a") is False)
    assert(sol.isMatch("aa", "aa") is True)
    assert(sol.isMatch("aaa", "aa") is False)
    assert(sol.isMatch("aa", "*") is True)
    assert(sol.isMatch("aa", "a*") is True)
    assert(sol.isMatch("ab", "?*") is True)
    assert(sol.isMatch("aab", "c*a*b") is False)
