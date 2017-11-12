# -*- coding: utf8 -*-
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters
#
# algorithms
# Hard (41.72%)
# Total Accepted:    31.1K
# Total Submissions: 74.7K
# Testcase Example:  '"eceba"'
#
#
# Given a string, find the length of the longest substring T that contains at
# most 2 distinct characters.
#
#
#
# For example,
#
# Given s = “eceba”,
#
#
#
# T is "ece" which its length is 3.
#
#


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        ans = j = 0
        table = {}
        for i in range(len(s)):
            while count <= 2 and j < len(s):
                if table.get(s[j], 0) == 0:
                    count += 1
                table[s[j]] = table.get(s[j], 0) + 1
                j += 1

            if count == 3:
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
    assert(sol.lengthOfLongestSubstringTwoDistinct("eceba") == 3)
