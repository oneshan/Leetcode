#
# [469] Convex Polygon
#
# https://leetcode.com/problems/convex-polygon
#
# algorithms
# Medium (33.05%)
# Total Accepted:    4.2K
# Total Submissions: 12.7K
# Testcase Example:  '[[0,0],[0,1],[1,1],[1,0]]'
#
# Given a list of points that form a polygon when joined sequentially, find if
# this polygon is convex (Convex polygon definition).
#
# Note:
#
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon
# (Simple polygon definition). In other words, we ensure that exactly two edges
# intersect at each vertex, and that edges otherwise don't intersect each
# other.
#
#
#
#
# Example 1:
#
# [[0,0],[0,1],[1,1],[1,0]]
#
# Answer: True
#
# Explanation:
#
#
#
# Example 2:
#
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
#
# Answer: False
#
# Explanation:
#
#
#


class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        prev = curr = 0
        points += points[:2]
        for i in range(2, len(points)):
            dx1 = points[i][0] - points[i - 1][0]
            dx2 = points[i][0] - points[i - 2][0]
            dy1 = points[i][1] - points[i - 1][1]
            dy2 = points[i][1] - points[i - 2][1]
            curr = dx1 * dy2 - dx2 * dy1
            if curr == 0:
                continue
            if prev * curr < 0:
                return False
            prev = curr
        return True

if __name__ == "__main__":
    sol = Solution()
    arr = [[0, 0], [0, 1], [1, 1], [1, 0]]
    assert(sol.isConvex(arr) is True)
    arr = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
    assert(sol.isConvex(arr) is False)
    arr = [[0, 0], [0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3], [3, 0]]
    assert(sol.isConvex(arr) is False)
    arr = [[0, -100], [4, -5], [5, -4], [5, 4], [4, 5], [-5, 5], [-5, -5]]
    assert(sol.isConvex(arr) is False)

