# -*- coding: utf8 -*-
#
# [505] The Maze II
#
# https://leetcode.com/problems/the-maze-ii
#
# algorithms
# Medium (37.81%)
# Total Accepted:    7.5K
# Total Submissions: 19.9K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
#
# Given the ball's start position, the destination and the maze, find the
# shortest distance for the ball to stop at the destination. The distance is
# defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the destination (included). If the ball cannot stop at
# the destination, return -1.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column
# indexes.
#
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: 12
# Explanation: One shortest way is : left -> down -> left -> down -> right ->
# down -> right.
# ⁠            The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
#
#
#
#
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: -1
# Explanation: There is no way for the ball to stop at the destination.
#
#
#
#
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not
# be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of
# the maze won't exceed 100.
#
#
#
import heapq


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1

        way = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(maze)
        n = len(maze[0])

        heap = []
        for d in range(4):
            heapq.heappush(heap, (0, start[0], start[1], d))

        visited = set()
        while heap:
            step, x, y, d = heapq.heappop(heap)
            if (x, y, d) in visited:
                continue
            visited.add((x, y, d))
            if x == destination[0] and y == destination[1]:
                return step

            while 0 <= x + way[d][0] < m and 0 <= y + way[d][1] < n:
                if maze[x + way[d][0]][y + way[d][1]] == 1:
                    break
                x += way[d][0]
                y += way[d][1]
                step += 1
            heapq.heappush(heap, (step, x, y, (d + 1) % 4))
            heapq.heappush(heap, (step, x, y, (d + 3) % 4))

        return -1


if __name__ == "__main__":
    sol = Solution()

    maze = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    assert(sol.shortestDistance(maze, [0, 4], [4, 4]) is 12)
    assert(sol.shortestDistance(maze, [0, 4], [3, 2]) is -1)
