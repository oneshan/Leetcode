#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water
#
# Medium (36.39%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            ans = max(ans, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 1]))
    print(sol.maxArea([1, 2, 3, 4, 5]))
    print(sol.maxArea([5, 4, 3, 2, 1]))
    print(sol.maxArea([1, 5, 3, 2, 4]))
