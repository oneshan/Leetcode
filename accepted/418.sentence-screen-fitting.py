# -*- coding: utf8 -*-
#
# [418] Sentence Screen Fitting
#
# https://leetcode.com/problems/sentence-screen-fitting
#
# algorithms
# Medium (27.84%)
# Total Accepted:    14.5K
# Total Submissions: 52.1K
# Testcase Example:  '["hello","world"]\n2\n8'
#
# Given a rows x cols screen and a sentence represented by a list of non-empty
# words, find how many times the given sentence can be fitted on the screen.
#
#
# Note:
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
#
#
#
#
# Example 1: 
#
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
#
# Output: 
# 1
#
# Explanation:
# hello---
# world---
#
# The character '-' signifies an empty space on the screen.
#
#
#
#
# Example 2: 
#
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
#
# Output: 
# 2
#
# Explanation:
# a-bcd- 
# e-a---
# bcd-e-
#
# The character '-' signifies an empty space on the screen.
#
#
#
#
# Example 3: 
#
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
#
# Output: 
# 1
#
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# The character '-' signifies an empty space on the screen.
#
#
#


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        lens, i, n = [len(s) + 1 for s in sentence], 0, len(sentence)
        total = sum(lens)
        ans = 0
        for _ in range(rows):
            remains = cols + 1
            while remains >= lens[i]:
                remains -= lens[i]
                i += 1
                if i == n:
                    ans += (1 + remains // total)
                    remains %= total
                    i = 0
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.wordsTyping(["I", "had", "apple", "pie"], 4, 5) == 1)
    assert(sol.wordsTyping(["try", "to", "be", "better"], 10000, 9001) == 5293333)
