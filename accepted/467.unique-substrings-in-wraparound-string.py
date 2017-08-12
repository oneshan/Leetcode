#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string
#
# Medium (32.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
#
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
#
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
#
# Example 1:
#
# Input: "a"
# Output: 1
#
# Explanation: Only the substring "a" of string "a" is in the string s.
#
#
#
# Example 2:
#
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
#
#
#
# Example 3:
#
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.
#
#
#


class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        count = 1
        table = {p[0]: 1}

        for i in range(1, len(p)):
            diff = ord(p[i]) - ord(p[i - 1])
            if diff == 1 or diff == -25:
                count += 1
            else:
                count = 1
            table[p[i]] = max(table.get(p[i], 0), count)

        return sum(table.values())


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findSubstringInWraproundString('zab') == 6)
    assert(sol.findSubstringInWraproundString('cac') == 2)
