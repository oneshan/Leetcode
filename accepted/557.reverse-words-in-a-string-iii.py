#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii
#
# Easy (60.08%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"Let\'s take LeetCode contest"'
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
#
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
#
#
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
#
#


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        start, end, n = 0, 0, len(s)
        while end < n:
            while end < n and s[end] != ' ':
                end += 1
            i, j = start, end - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            start = end = end + 1
        return ''.join(s)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
