#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix
#
# Easy (31.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
#


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort()
        j = 0
        while j < len(strs[0]) and j < len(strs[-1]) and strs[0][j] == strs[-1][j]:
            j += 1
        return strs[0][:j]


if __name__ == "__main__":
    sol = Solution()
    arr = ['abcde', 'abc', 'abcd', 'abcc', 'abcdf']
    print(sol.longestCommonPrefix(arr))
