#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii
#
# algorithms
# Medium (27.27%)
# Total Accepted:    32.7K
# Total Submissions: 120K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
#
# Given an input string, reverse the string word by word. A word is defined as
# a sequence of non-space characters.
#
#
#
# The input string does not contain leading or trailing spaces and the words
# are always separated by a single space.
#
#
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
#
#
# Could you do it in-place without allocating extra space?
#
#
# Related problem: Rotate Array
#
#
# Update (2017-10-16):
# We have updated the function signature to accept a character array, so please
# reset to the default code definition by clicking on the reload button above
# the code editor. Also, Run Code is now available!
#
#


class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverse(str, 0, len(str) - 1)
        p1, p2 = 0, 0
        while p2 < len(str):
            while p2 < len(str) and str[p2] != ' ':
                p2 += 1
            self.reverse(str, p1, p2 - 1)
            p1 = p2 = p2 + 1

    def reverse(self, str, i, j):
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    sol = Solution()
    str = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    sol.reverseWords(str)
    print(str)
