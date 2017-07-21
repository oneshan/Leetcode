#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions
#
# Medium (18.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["XXXX","XOOX","XXOX","XOXX"]'
#
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
#
#
# For example,
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
#
#
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
#


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        queue = []
        for i in range(m):
            if board[i][0] == 'O':
                queue += (i, 0),
            if board[i][-1] == 'O':
                queue += (i, n - 1),
        for j in range(n):
            if board[0][j] == 'O':
                queue += (0, j),
            if board[-1][j] == 'O':
                queue += (m - 1, j),

        while queue:
            row, col = queue.pop(0)
            if board[row][col] == 'O':
                board[row][col] = 'N'
                if row - 1 >= 0 and board[row - 1][col] == 'O':
                    queue += (row - 1, col),
                if row + 1 < m and board[row + 1][col] == 'O':
                    queue += (row + 1, col),
                if col - 1 >= 0 and board[row][col - 1] == 'O':
                    queue += (row, col - 1),
                if col + 1 < n and board[row][col + 1] == 'O':
                    queue += (row, col + 1),

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


if __name__ == "__main__":
    sol = Solution()
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    sol.solve(board)
    print(board)
