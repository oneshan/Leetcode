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
        
