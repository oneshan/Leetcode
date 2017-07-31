#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area
#
# Medium (32.65%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '-2\n-2\n2\n2\n-2\n-2\n2\n2'
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
# 
# 
# 
# 
# Assume that the total area is never beyond the maximum possible value of
# int.
# 
# 
# Credits:Special thanks to @mithmatt for adding this problem, creating the
# above image and all test cases.
#
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        over_x = max(0, min(C, G) - max(A, E))
        over_y = max(0, min(D, H) - max(B, F))
        overlap = over_x * over_y

        return area1 + area2 - overlap


if __name__ == "__main__":
    sol = Solution()
    assert(sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45)
