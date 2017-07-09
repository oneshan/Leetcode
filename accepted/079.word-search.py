#
# [79] Word Search
#
# https://leetcode.com/problems/word-search
#
# Medium (26.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["ABCE","SFCS","ADEE"]\n"ABCCED"'
#
# 
# Given a 2D board and a word, find if the word exists in the grid.
# 
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# 
# For example,
# Given board = 
# 
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
# 
#


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False

        m = len(board)
        n = len(board[0])
        wordlen = len(word)

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == wordlen - 1:
                return True

            temp = board[i][j]
            board[i][j] = None
            hasFound = (
                (i > 0 and dfs(i - 1, j, k + 1)) or
                (i < m - 1 and dfs(i + 1, j, k + 1)) or
                (j > 0 and dfs(i, j - 1, k + 1)) or
                (j < n - 1 and dfs(i, j + 1, k + 1))
            )
            board[i][j] = temp
            return hasFound

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(sol.exist(board, word))
    word = "SEE"
    print(sol.exist(board, word))
    word = "ABCB"
    print(sol.exist(board, word))
