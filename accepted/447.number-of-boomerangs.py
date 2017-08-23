#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs
#
# Easy (44.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#
#
#


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        ans = 0
        for p1 in points:
            table = {}
            for p2 in points:
                dist = distance(p1, p2)
                table[dist] = table.get(dist, 0) + 1
            for key in table:
                ans += table[key] * (table[key] - 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]) == 2)
