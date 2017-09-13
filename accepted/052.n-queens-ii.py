#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii
#
# Hard (44.28%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of
# distinct solutions.
#
#
#


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        loc = [-1] * n

        def check(k, j):
            for i in range(k):
                if loc[i] == j or abs(k - i) == abs(j - loc[i]):
                    return False
            return True

        def dfs(i):
            if i == n:
                self.ans += 1
                return
            for j in range(n):
                if check(i, j):
                    loc[i] = j
                    dfs(i + 1)

        dfs(0)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.totalNQueens(4) == 2)
