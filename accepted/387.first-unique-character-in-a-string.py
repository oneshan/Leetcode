#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string
#
# Easy (46.38%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"leetcode"'
#
#
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#
#


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        table = {}
        n = len(s)
        for idx, ch in enumerate(s):
            if ch not in table:
                table[ch] = idx
            else:
                table[ch] = n

        ans = n
        for ch in table:
            ans = min(ans, table[ch])

        return ans if ans < n else -1


if __name__ == "__main__":
    sol = Solution()
    assert(sol.firstUniqChar("leetcode") == 0)
    assert(sol.firstUniqChar("loveleetcode") == 2)
    assert(sol.firstUniqChar("leetcodeleetcode") == -1)
