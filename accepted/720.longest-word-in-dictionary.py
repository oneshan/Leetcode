#
# [720] Longest Word in Dictionary
#
# https://leetcode.com/problems/longest-word-in-dictionary
#
# algorithms
# Easy (40.64%)
# Total Accepted:    5.5K
# Total Submissions: 13.7K
# Testcase Example:  '["w","wo","wor","worl","world"]'
#
# Given a list of strings words representing an English Dictionary, find the
# longest word in words that can be built one character at a time by other
# words in words.  If there is more than one possible answer, return the
# longest word with the smallest lexicographical order.  If there is no answer,
# return the empty string.
#
# Example 1:
#
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor",
# and "worl".
#
#
#
# Example 2:
#
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary.
# However, "apple" is lexicographically smaller than "apply".
#
#
#
# Note:
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
#
#


class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isWord = False


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.isWord = True

    def search(self):
        queue = [(self.root, "")]
        ans = ""
        while queue:
            size = len(queue)
            for _ in range(size):
                node, word = queue.pop(0)
                ans = min(ans, word) if len(ans) == len(word) else word
                for ch in node.child:
                    if node.child[ch].isWord:
                        queue.append((node.child[ch], word + ch))
        return ans


class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = TrieTree()
        for word in words:
            trie.insert(word)
        return trie.search()

if __name__ == "__main__":
    sol = Solution()
    arr = ["w", "wo", "wor", "worl", "world"]
    assert(sol.longestWord(arr) == "world")
    arr = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    assert(sol.longestWord(arr) == "apple")
