# -*- coding: utf8 -*-
#
# [351] Android Unlock Patterns
#
# https://leetcode.com/problems/android-unlock-patterns
#
# algorithms
# Medium (44.10%)
# Total Accepted:    16.2K
# Total Submissions: 36.8K
# Testcase Example:  '1\n1'
#
#
# Given an Android 3x3 key lock screen and two integers m and n, where  1 ≤ m ≤
# n ≤ 9, count the total number of unlock patterns of the Android lock screen,
# which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
#
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any
# other keys, the other keys must have previously selected in the pattern. No
# jumps through non selected key is allowed.
# The order of keys used matters.
#
#
#
#
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
#
#
# Invalid move: 4 - 1 - 3 - 6 
#
# Line  1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
#
# Line  1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
#
# Line 1 - 3 is valid because it passes through key 2, which had been selected
# in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
#
# Line 1 - 9 is valid because it passes through key 5, which had been selected
# in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jump = {}
        jump[(1, 3)] = jump[(3, 1)] = 2
        jump[(4, 6)] = jump[(6, 4)] = 5
        jump[(7, 9)] = jump[(9, 7)] = 8
        jump[(1, 7)] = jump[(7, 1)] = 4
        jump[(2, 8)] = jump[(8, 2)] = 5
        jump[(3, 9)] = jump[(9, 3)] = 6
        jump[(1, 9)] = jump[(9, 1)] = 5
        jump[(3, 7)] = jump[(7, 3)] = 5

        visited = [False] * 10
        visited[0] = True

        def dfs(i, lens, count):
            if lens >= m:
                count += 1
            if lens == n:
                return count

            visited[i] = True
            for j in range(1, 10):
                mid = jump.get((i, j), 0)
                if not visited[j] and visited[mid]:
                    count = dfs(j, lens + 1, count)
            visited[i] = False

            return count

        return dfs(1, 1, 0) * 4 + dfs(2, 1, 0) * 4 + dfs(5, 1, 0)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.numberOfPatterns(1, 1) == 9)
