#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water
#
# Hard (36.42%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after
# raining. 
#
#
#
# For example, 
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
#
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                ans += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trap(arr))
