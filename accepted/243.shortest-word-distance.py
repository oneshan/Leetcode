#
# [243] Shortest Word Distance
#
# https://leetcode.com/problems/shortest-word-distance
#
# algorithms
# Easy (52.83%)
# Total Accepted:    36.1K
# Total Submissions: 68.3K
# Testcase Example:  '["a","b"]\n"a"\n"b"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
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


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p1 = p2 = 0
        ans = len(words)
        for idx, word in enumerate(words, 1):
            if word == word1:
                p1 = idx
            elif word == word2:
                p2 = idx
            else:
                continue
            if p1 and p2:
                ans = min(ans, abs(p2 - p1))
        return ans


if __name__ == "__main__":
    sol = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]
    assert(sol.shortestDistance(words, "coding", "practice") == 3)
    assert(sol.shortestDistance(words, "makes", "coding") == 1)
