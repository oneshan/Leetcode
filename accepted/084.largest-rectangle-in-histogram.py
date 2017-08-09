#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram
#
# Hard (26.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,1,5,6,2,3]'
#
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
#
#


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        stack = []
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                j = stack.pop()
                k = i - stack[-1] - 1 if stack else i
                ans = max(ans, heights[j] * k)
            stack.append(i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10)
    assert(sol.largestRectangleArea([2, 1, 2]) == 3)
    assert(sol.largestRectangleArea([4, 2, 0, 3, 2, 5]) == 6)
