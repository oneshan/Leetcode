#
# [245] Shortest Word Distance III
#
# https://leetcode.com/problems/shortest-word-distance-iii
#
# algorithms
# Medium (50.65%)
# Total Accepted:    23.1K
# Total Submissions: 45.5K
# Testcase Example:  '["a","b"]\n"a"\n"b"'
#
# This is a follow up of Shortest Word Distance. The only difference is now
# word1 could be the same as word2.
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in
# the list.
# For example,
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Given word1 = "makes", word2 = "coding", return 1.
# Given word1 = "makes", word2 = "makes", return 3.
#
#
#
# Note:
# You may assume word1 and word2 are both in the list.
#
#


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
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
                if p1 and word == word2:
                    ans = min(ans, idx - p1)
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
    assert(sol.shortestWordDistance(words, "coding", "practice") == 3)
    assert(sol.shortestWordDistance(words, "makes", "makes") == 3)
