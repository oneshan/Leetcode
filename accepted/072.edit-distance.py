#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance
#
# Hard (31.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""'
#
#
# Given two words word1 and word2, find the minimum number of steps required to
# convert word1 to word2. (each operation is counted as 1 step.)
#
#
#
# You have the following 3 operations permitted on a word:
#
#
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],
                                       dp[i - 1][j],
                                       dp[i - 1][j - 1]
                                       )
        return dp[m][n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("", ""))
    print(sol.minDistance("1", ""))
    print(sol.minDistance("", "1"))
    print(sol.minDistance("1a34", "5b18"))
