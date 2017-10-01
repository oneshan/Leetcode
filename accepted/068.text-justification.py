# -*- coding: utf-8 -*- 
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification
#
# Hard (18.80%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[""]\n0'
#
#
# Given an array of words and a length L, format the text such that each line
# has exactly L characters and is fully (left and right) justified.
# ⁠
#
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly L characters.
#
#
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the
# right.
#
#
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
#
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
#
#
# Return the formatted lines as:
#
# [
# ⁠  "This    is    an",
# ⁠  "example  of text",
# ⁠  "justification.  "
# ]
#
#
#
#
# Note: Each word is guaranteed not to exceed L in length.
#
#
#
# click to show corner cases.
#
# Corner Cases:
#
#
# A line other than the last line might contain only one word. What should you
# do in this case?
# In this case, that line should be left-justified.
#
#
#


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []

        n, i = len(words), 0
        ans = []

        while i < n:

            # find start and end of word indexes
            idx, lens = i, 0
            while idx < n:
                if lens + len(words[idx]) > maxWidth:
                    break
                idx, lens = idx + 1, lens + len(words[idx]) + 1
            lens -= 1

            # left justified -- last line or one word
            if idx == n or idx == i + 1:
                line = ' '.join(words[i:idx]) + ' ' * (maxWidth - lens)
            # fully justified -- multi-words
            else:
                k = (maxWidth - lens) // (idx - i - 1)
                m = (maxWidth - lens) % (idx - i - 1)
                line = words[i]
                for j in range(1, idx - i):
                    if j <= m:
                        line += ' '
                    line += ' ' * (k + 1) + words[i + j]

            ans.append(line)
            i = idx

        return ans

if __name__ == "__main__":
    sol = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(sol.fullJustify(words, 16))
