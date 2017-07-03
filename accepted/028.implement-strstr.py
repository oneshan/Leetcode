#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr
#
# Easy (27.85%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""'
#
#
# Implement strStr().
#
#
# Returns the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
#


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenH = len(haystack)
        lenN = len(needle)

        if lenN == 0:
            return 0
        if lenN > lenH:
            return -1

        for i in range(lenH - lenN + 1):
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1
                if j == lenN:
                    return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    haystack, needle = "Test", ""
    print(sol.strStr(haystack, needle))
    haystack, needle = "Test", "TestT"
    print(sol.strStr(haystack, needle))
    haystack, needle = "Test", "st"
    print(sol.strStr(haystack, needle))
    haystack, needle = "Test", "esp"
    print(sol.strStr(haystack, needle))
