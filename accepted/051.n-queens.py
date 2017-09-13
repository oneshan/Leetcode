#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens
#
# Hard (30.48%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an nxn chessboard
# such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        loc = [-1] * n
        tmp = '.' * n
        self.ans = []

        def check(k, j):
            for i in range(k):
                if loc[i] == j or abs(k - i) == abs(j - loc[i]):
                    return False
            return True

        def dfs(i, table):
            if i == n:
                self.ans += table,
                return
            for j in range(n):
                if check(i, j):
                    loc[i] = j
                    dfs(i + 1, table + [tmp[:j] + 'Q' + tmp[j + 1:]])

        dfs(0, [])
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
