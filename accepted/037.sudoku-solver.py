#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver
#
# Hard (29.68%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.
#
#
#
# A sudoku puzzle...
#
#
#
#
# ...and its solution numbers marked in red.
#


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        listBoard = [list(string) for string in board]
        self.dfs(0, listBoard)
        for i in range(9):
            board[i] = ''.join(listBoard[i])

    def dfs(self, count, board):
        if count == 81:
            return True

        i, j = count // 9, count % 9
        if board[i][j] != '.':
            return self.dfs(count + 1, board)

        for n in "123456789":
            board[i][j] = n
            if self.check(i, j, board) and self.dfs(count + 1, board):
                return True
            board[i][j] = '.'
        return False

    def check(self, x, y, board):
        # check row
        for j in range(9):
            if y != j and board[x][j] == board[x][y]:
                return False
        # check column
        for i in range(9):
            if x != i and board[i][y] == board[x][y]:
                return False
        # check sub-box
        for i in range(9):
            new_x = x - x % 3 + i // 3
            new_y = y - y % 3 + i % 3
            if new_x != x and new_y != y and board[new_x][new_y] == board[x][y]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    board = [
        "..9748...",
        "7........",
        ".2.1.9...",
        "..7...24.",
        ".64.1.59.",
        ".98...3..",
        "...8.3.2.",
        "........6",
        "...2759.."
    ]
    sol.solveSudoku(board)
    print(board)
