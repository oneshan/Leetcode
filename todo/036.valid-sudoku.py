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
