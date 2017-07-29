#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree
#
# Medium (27.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["Trie","search"]\n[[],["a"]]'
#
#
# Implement a trie with insert, search, and startsWith methods.
#
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
#


class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.childs:
                return False
            node = node.childs[ch]
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.childs:
                return False
            node = node.childs[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    obj = Trie()
    obj.insert("Test")
    assert(obj.search("Test") is True)
    assert(obj.search("Tes") is False)
    assert(obj.search("Test1") is False)
    assert(obj.search("ABC") is False)
    assert(obj.startsWith("Tes") is True)
