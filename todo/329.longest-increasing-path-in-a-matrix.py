#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix
#
# Hard (36.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# 
# Example 1:
# 
# nums = [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# nums = [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# 
# 
# 
# 
# Return 4
# 
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not
# allowed.
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
