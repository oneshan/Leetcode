#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku
#
# Medium (35.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]'
#
# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with
# the character '.'.
#
#
#
# A partially filled sudoku which is valid.
#
#
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the
# filled cells need to be validated.
#
#


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and not self.check(i, j, board):
                    return False
        return True

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
        ".87654321",
        "2........",
        "3........",
        "4........",
        "5........",
        "6........",
        "7........",
        "8........",
        "9........"
    ]
    print(sol.isValidSudoku(board))
