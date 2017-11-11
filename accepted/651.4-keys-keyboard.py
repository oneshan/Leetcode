#
# [651] 4 Keys Keyboard
#
# https://leetcode.com/problems/4-keys-keyboard
#
# algorithms
# Medium (48.36%)
# Total Accepted:    4.4K
# Total Submissions: 9.2K
# Testcase Example:  '1'
#
# Imagine you have a special keyboard with the following keys: 
# Key 1: (A):  Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already
# been printed. 
#
#
#
# Now, you can only press the keyboard for N times (with the above four keys),
# find out the maximum numbers of 'A' you can print on screen.
#
#
# Example 1:
#
# Input: N = 3
# Output: 3
# Explanation:
# We can at most get 3 A's on screen by pressing following key sequence:
# A, A, A
#
#
#
# Example 2:
#
# Input: N = 7
# Output: 9
# Explanation: 
# We can at most get 9 A's on screen by pressing following key sequence:
# A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
#
#
#
# Note:
#
# 1 <= N <= 50 
# Answers will be in the range of 32-bit signed integer.
#
#
#
#
from collections import defaultdict


class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i][j] = ith command, j buffer
        dp = [defaultdict(int) for _ in range(N + 2)]
        dp[0][0] = 0
        for i in range(N):
            for j in dp[i]:
                # Type 'A' or ctrl + V
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + 1, dp[i][j] + j)
                # ctrl + A & ctrl + C
                dp[i + 2][dp[i][j]] = max(dp[i + 2][dp[i][j]], dp[i][j])
        return max(dp[N].values())

if __name__ == "__main__":
    sol = Solution()
    assert(sol.maxA(7) == 9)
