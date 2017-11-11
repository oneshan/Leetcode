# -*- coding: utf8 -*-
#
# [531] Lonely Pixel I
#
# https://leetcode.com/problems/lonely-pixel-i
#
# algorithms
# Medium (55.26%)
# Total Accepted:    7.6K
# Total Submissions: 13.8K
# Testcase Example:  '[["W","W","B"],["W","B","W"],["B","W","W"]]'
#
# Given a picture consisting of black and white pixels, find the number of
# black lonely pixels.
#
# The picture is represented by a 2D char array consisting of 'B' and 'W',
# which means black and white pixels respectively.
#
# A black lonely pixel is character 'B' that located at a specific position
# where the same row and same column don't have any other black pixels.
#
# Example:
#
# Input:
# [['W', 'W', 'B'],
# ⁠['W', 'B', 'W'],
# ⁠['B', 'W', 'W']]
#
# Output: 3
# Explanation: All the three 'B's are black lonely pixels.
#
#
#
# Note:
#
# The range of width and height of the input 2D array is [1,500].
#
#
#


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if not picture or not picture[0]:
            return 0

        m = len(picture)
        n = len(picture[0])
        rows = [0] * m
        cols = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    if rows[i] == 1 and cols[j] == 1:
                        ans += 1

        return ans

if __name__ == "__main__":
    matrix = [
        ['W', 'W', 'B'],
        ['W', 'B', 'W'],
        ['B', 'W', 'W']
    ]
    sol = Solution()
    assert(sol.findLonelyPixel(matrix) == 3)

    matrix = [
        ['B', 'B'],
        ['B', 'B']
    ]
    assert(sol.findLonelyPixel(matrix) == 0)
