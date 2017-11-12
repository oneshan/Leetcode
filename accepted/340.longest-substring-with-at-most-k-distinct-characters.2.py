# -*- coding: utf8 -*-
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters
#
# algorithms
# Hard (39.08%)
# Total Accepted:    28.6K
# Total Submissions: 73.2K
# Testcase Example:  '"eceba"\n2'
#
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
#
#
#
# For example,
#
# Given s = “eceba” and k = 2,
#
#
#
# T is "ece" which its length is 3.
#
#


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0

        table = {}
        count = 0
        j = ans = 0

        for i, ch in enumerate(s):
            while count <= k and j < len(s):
                if table.get(s[j], 0) == 0:
                    count += 1
                table[s[j]] = table.get(s[j], 0) + 1
                j += 1

            if count > k:
                ans = max(ans, j - i - 1)
            else:
                ans = max(ans, j - i)

            if j == len(s):
                break

            table[s[i]] -= 1
            if table[s[i]] == 0:
                count -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.lengthOfLongestSubstringKDistinct("eceba", 2) == 3)
    assert(sol.lengthOfLongestSubstringKDistinct("a", 1) == 1)
    assert(sol.lengthOfLongestSubstringKDistinct("abaccc", 2) == 4)
    assert(sol.lengthOfLongestSubstringKDistinct("aba", 1) == 1)
