#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways
#
# Medium (19.42%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#
# Given an encoded message containing digits, determine the total number of
# ways to decode it.
#
#
#
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
#
#
#
# The number of ways decoding "12" is 2.
#
#


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0

        preTwo, preOne = 0, 1
        for idx, ch in enumerate(s):
            cur = 0
            if ch != '0':
                cur += preOne
            if idx and 10 <= int(s[idx - 1:idx + 1]) <= 26:
                cur += preTwo
            preTwo, preOne = preOne, cur
        return preOne


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("100"))   # 0
    print(sol.numDecodings("101"))   # 1 [10 1]
    print(sol.numDecodings("12"))    # 2 [1 2], [12]
    print(sol.numDecodings("123"))   # 3 [1 2 3], [12 3], [1 23]
    print(sol.numDecodings("1231"))  # 3 [1 2 3 1], [12 3 1], [1 23 1]
