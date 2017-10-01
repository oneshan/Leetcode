#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words
#
# Medium (48.80%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
#
#
#
#
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
#
#
#
# You need to output the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
#
#
# Note:
#
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
#
#
#


class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for idx, ch in enumerate(word):
            if ch not in node.child:
                break
            node = node.child[ch]
            if node.isWord:
                break
        return word[:idx + 1] if node.isWord else word


class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        tree = Trie()
        for word in dict:
            tree.insert(word)
        return " ".join(tree.search(word) for word in sentence.split())


if __name__ == "__main__":
    sol = Solution()
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(sol.replaceWords(dict, sentence))
    dict = ["a", "aa", "aaa", "bac"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    print(sol.replaceWords(dict, sentence))
