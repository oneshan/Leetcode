#
# [161] One Edit Distance
#
# https://leetcode.com/problems/one-edit-distance
#
# algorithms
# Medium (31.53%)
# Total Accepted:    41.1K
# Total Submissions: 130.3K
# Testcase Example:  '""\n""'
#
# Given two strings S and T, determine if they are both one edit distance apart.
#


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t:
            return False

        n1, n2 = len(s), len(t)
        if n2 > n1:
            n1, n2, s, t = n2, n1, t, s
        if n1 - n2 > 1:
            return False

        p1 = p2 = 0
        modified = False
        while p1 < n1 and p2 < n2:
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            elif modified:
                return False
            elif n1 == n2:  # replace
                p1 += 1
                p2 += 1
                modified = True
            else:           # insert
                p1 += 1
                modified = True

        if not modified and n1 == n2 + 1:
            return True
        return modified


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isOneEditDistance("", "") is False)
    assert(sol.isOneEditDistance("abc", "abd") is True)
    assert(sol.isOneEditDistance("ac", "abc") is True)
    assert(sol.isOneEditDistance("abc", "bc") is True)
    assert(sol.isOneEditDistance("c", "c") is False)
    assert(sol.isOneEditDistance("ac", "c") is True)
    assert(sol.isOneEditDistance("", "c") is True)
