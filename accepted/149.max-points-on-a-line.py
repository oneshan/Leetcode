#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line
#
# Hard (15.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class Solution(object):
    
    def gcd(self, x, y):
        if y == 0:
            return x
        return self.gcd(y, x % y)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        if n <= 1:
            return n

        ans = 0
        for i in range(n):
            slope = {}
            count_dup = count_inf = 0

            for j in range(i, n):
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                if dx == 0 and dy == 0:
                    count_dup += 1
                if dx == 0:
                    count_inf += 1
                else:
                    tmp = self.gcd(dx, dy)
                    s = (dx // tmp, dy // tmp)
                    slope[s] = slope.get(s, 0) + 1

            ans = max(ans, count_inf)
            for s in slope:
                ans = max(ans, slope[s] + count_dup)

        return ans
