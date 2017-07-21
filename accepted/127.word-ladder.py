#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder
#
# Medium (19.32%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
#
# For example,
#
#
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
#
#
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
#
#
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
#
#
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
#
#


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        wordLen = len(beginWord)
        queue = [(beginWord, 1)]
        while queue:
            currWord, count = queue.pop(0)
            if currWord == endWord:
                return count
            for i in range(wordLen):
                part1, part2 = currWord[:i], currWord[i + 1:]
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = part1 + ch + part2
                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, count + 1))
        return 0


if __name__ == "__main__":
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(sol.ladderLength(beginWord, endWord, wordList))
