#
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string
#
# algorithms
# Medium (38.67%)
# Total Accepted:    4.7K
# Total Submissions: 12.1K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them.
#
# Example 1:
#
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#
#
#
# Example 2:
#
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
#
#
# Note:
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
#
#
#


class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        start = end = -1
        ans = ""

        for i, ch in enumerate(s):
            maxlen = 0
            for word in dict:
                if s[i:].startswith(word):
                    maxlen = max(maxlen, len(word))

            if maxlen:
                if start == -1:
                    start = i
                end = max(end, i + maxlen)
                continue

            if i == end:
                ans += '<b>{}</b>'.format(s[start:end])
                start = end = -1
            
            if start == -1:
                ans += ch

        if start != -1:
            ans += '<b>{}</b>'.format(s[start:end])

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "aaabbcc"
    dict = ["aaa", "aab", "bc"]
    assert(sol.addBoldTag(s, dict) == "<b>aaabbc</b>c")

    s = "abcxyz123"
    dict = ["abc", "123"]
    assert(sol.addBoldTag(s, dict) == "<b>abc</b>xyz<b>123</b>")
