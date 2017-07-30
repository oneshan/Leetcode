#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design
#
# Medium (22.17%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
#
# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
#
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one
# letter.
#
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
#
# click to show hint.
#
# You should be familiar with how a Trie works. If not, please work on this
# problem: Implement Trie (Prefix Tree) first.
#
#


class TrieNode(object):

    def __init__(self):
        self.childs = {}
        self.isWord = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            if ch not in node.childs:
                node.childs[ch] = TrieNode()
            node = node.childs[ch]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        return self.recur(self.root, word, 0)

    def recur(self, node, word, idx):
        if idx == len(word):
            return node.isWord

        if word[idx] == '.':
            for ch in node.childs:
                if self.recur(node.childs[ch], word, idx + 1):
                    return True
        elif word[idx] in node.childs:
            return self.recur(node.childs[word[idx]], word, idx + 1)

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("test")
    assert(obj.search("te.t") is True)
    assert(obj.search("t.tt") is False)
