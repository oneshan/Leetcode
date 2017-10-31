#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life
#
# Medium (36.72%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[]]'
#
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
#
#
#
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
#
#
#
#
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
#
#
#
#
# Write a function to compute the next state (after one update) of the board
# given its current state.
#
#
# Follow up: 
#
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#
from collections import defaultdict

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                cnt = self.count(board, i, j)
                if board[i][j] > 0:
                    if cnt < 2 or cnt > 3:
                        board[i][j] = 2
                elif cnt == 3:
                    board[i][j] = -1

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == -1:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0

    def count(self, board, i, j):
        cnt = 0
        for dx in -1, 0, 1:
            for dy in -1, 0, 1:
                if dx == dy == 0:
                    continue
                if 0 <= i + dx < self.m and 0 <= j + dy < self.n:
                    cnt += int(board[i + dx][j + dy] > 0)
        return cnt
