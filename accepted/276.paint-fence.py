#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence
#
# algorithms
# Easy (34.64%)
# Total Accepted:    26.7K
# Total Submissions: 77.2K
# Testcase Example:  '0\n0'
#
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k

        # dp[0] = 0, dp[1] = k, dp[2] = k * k
        # dp[i] = dp[i-2] * (k - 1) + dp[i-1] * (k - 1)
        preTwo, preOne = k, k * k
        for _ in range(2, n):
            preTwo, preOne = preOne, (preOne + preTwo) * (k - 1)
        return preOne

if __name__ == "__main__":
    sol = Solution()
    assert(sol.numWays(0, 0) == 0)
    assert(sol.numWays(3, 2) == 6)
