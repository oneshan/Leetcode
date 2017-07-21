#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii
#
# Hard (13.98%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
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
# Return
#
# ⁠ [
# ⁠   ["hit","hot","dot","dog","cog"],
# ⁠   ["hit","hot","lot","log","cog"]
# ⁠ ]
#
#
#
#
# Note:
#
# Return an empty list if there is no such transformation sequence.
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
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordLen = len(beginWord)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return []

        graph = {word: [] for word in wordSet}  # value: parents of word

        curr_level = set([beginWord])
        while curr_level and endWord not in curr_level:
            prev_level = curr_level
            curr_level = set()
            for word in prev_level:
                wordSet.remove(word)
            for word in prev_level:
                for i in range(wordLen):
                    part1, part2 = word[:i], word[i + 1:]
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = part1 + ch + part2
                        if newWord in wordSet:
                            graph[newWord].append(word)
                            curr_level.add(newWord)

        ans = [[endWord]]
        while ans and ans[0][0] != beginWord:
            ans = [[p] + words for words in ans for p in graph[words[0]]]
        return ans


if __name__ == "__main__":
    sol = Solution()
    wordList = ["hot", "dot", "dog", "lot", "log"]
    beginWord = "hot"
    endWord = "cog"

    print(sol.findLadders(beginWord, endWord, wordList))
