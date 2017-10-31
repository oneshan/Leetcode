#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii
#
# algorithms
# Medium (39.10%)
# Total Accepted:    25.5K
# Total Submissions: 65.3K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# This is a follow up of Shortest Word Distance. The only difference is now you
# are given the list of words and your method will be called repeatedly many
# times with different parameters. How would you optimize it?
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list.
#
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
#
# Given word1 = "coding", word2 = "practice", return 3.
# Given word1 = "makes", word2 = "coding", return 1.
#
#
#
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
#
#
from collections import defaultdict


class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.table = defaultdict(list)
        for idx, word in enumerate(words, 1):
            self.table[word].append(idx)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = self.table[word1]
        l2 = self.table[word2]
        n1, n2 = len(l1), len(l2)
        p1 = p2 = 0
        ans = float('inf')
        while p1 < n1 and p2 < n2:
            if l1[p1] < l2[p2]:
                ans = min(ans, l2[p2] - l1[p1])
                p1 += 1
            else:
                ans = min(ans, l1[p1] - l2[p2])
                p2 += 1
        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    obj = WordDistance(words)
    assert(obj.shortest("coding", "practice") == 3)
    assert(obj.shortest("makes", "coding") == 1)
