# -*- coding: utf8 -*-
#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection
#
# algorithms
# Medium (30.16%)
# Total Accepted:    12K
# Total Submissions: 39.9K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
#
#
# ⁠   Example 1:
#
#
# Given points = [[1,1],[-1,1]], return true.
#
#
#
# ⁠   Example 2:
#
#
# Given points = [[1,1],[-1,-1]], return false.
#
#
# Follow up:
# Could you do better than O(n2)?
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True

        table = set()
        line = 0.0
        for point in points:
            if (point[0], point[1]) not in table:
                table.add((point[0], point[1]))
                line += point[0]
        line /= len(table)

        for point in table:
            if (2 * line - point[0], point[1]) not in table:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    assert(sol.isReflected([[1, 1], [-1, 1]]) is True)
    assert(sol.isReflected([[1, 1], [-1, -1]]) is False)
    assert(sol.isReflected([[-16, 1], [16, 1], [16, 1]]) is True)
    assert(sol.isReflected([[1, 1], [1, 1], [1, 1]]) is True)
    assert(sol.isReflected([[0, 0], [1, 0]] is True))
