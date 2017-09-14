#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string
#
# Hard (24.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""\n""'
#
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
#
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#
#


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False

        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(n1):
            dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]

        for j in range(n2):
            dp[0][j + 1] = dp[0][j] and s2[j] == s3[j]

        for i in range(n1):
            for j in range(n2):
                dp[i + 1][j + 1] = (dp[i][j + 1] and s1[i] == s3[i + j + 1]) or \
                                   (dp[i + 1][j] and s2[j] == s3[i + j + 1])

        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isInterleave("a", "", "a") is True)
    assert(sol.isInterleave("", "b", "b") is True)

    s1 = "aabcc"
    s2 = "dbbca"
    assert(sol.isInterleave(s1, s2, "aadbbcbcac") is True)
    assert(sol.isInterleave(s1, s2, "aadbbbaccc") is False)
