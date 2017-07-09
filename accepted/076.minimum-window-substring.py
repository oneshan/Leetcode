#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring
#
# Hard (24.90%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"a"\n"a"'
#
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
#
#
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
#
#
# Minimum window is "BANC".
#
#
#
# Note:
# If there is no such window in S that covers all characters in T, return the
# empty string "".
#
#
# If there are multiple such windows, you are guaranteed that there will always
# be only one unique minimum window in S.
#
#


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        window = {}
        count = len(t)
        for ch in t:
            window[ch] = window.get(ch, 0) + 1

        p1 = begin = end = 0
        for p2, ch in enumerate(s, 1):
            window[ch] = window.get(ch, 0) - 1
            if window[ch] >= 0:
                count -= 1
            if count == 0:
                while window[s[p1]] < 0:
                    window[s[p1]] += 1
                    p1 += 1
                if not end or end - begin > p2 - p1:
                    begin, end = p1, p2
                window[s[p1]] += 1
                count = 1
                p1 += 1

        return s[begin: end]

if __name__ == "__main__":
    sol = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(sol.minWindow(S, T))
    T = "X"
    print(sol.minWindow(S, T))
