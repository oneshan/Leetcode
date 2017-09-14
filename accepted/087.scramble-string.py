# -*- coding: utf-8 -*-
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string
#
# Hard (28.89%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"a"\n"a"'
#
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
#
#
# Below is one possible representation of s1 = "great":
#
#    great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
#
#
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
#
#
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
#
#
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
#
#
# We say that "rgeat" is a scrambled string of "great".
#
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
#
#
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
#
#
# We say that "rgtae" is a scrambled string of "great".
#
#
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
#
#


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False

        table = {}
        n = len(s1)
        for i in range(n):
            table[s1[i]] = table.get(s1[i], 0) + 1
            table[s2[i]] = table.get(s2[i], 0) - 1
        for ch in table:
            if table[ch]:
                return False

        for i in range(1, n):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isScramble("rgtae", "great") is True)
