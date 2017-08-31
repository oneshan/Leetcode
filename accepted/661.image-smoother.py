#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother
#
# Easy (48.17%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
#
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
#
#
# Note:
#
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
#
#


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])

        ans = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                _sum = _num = 0
                for dx in (-1, 0, 1):
                    if 0 > x + dx or x + dx == m:
                        continue
                    for dy in (-1, 0, 1):
                        if 0 <= y + dy < n:
                            _sum += M[x + dx][y + dy]
                            _num += 1

                ans[x][y] = _sum // _num

        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    ans = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    assert(sol.imageSmoother(arr) == ans)
