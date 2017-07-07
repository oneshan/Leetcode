#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors
#
# Medium (37.64%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
#
# Given an array with n objects colored red, white or blue, sort them so that
# objects of the same color are adjacent, with the colors in the order red,
# white and blue.
#
#
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
#
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
#
# click to show follow up.
#
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
#


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, len(nums) - 1, 0
        while k <= j:
            if nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            elif nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            else:
                k += 1
        # print(nums)


if __name__ == "__main__":
    sol = Solution()
    sol.sortColors([0, 1, 2, 0, 1, 2, 0, 1])
    sol.sortColors([2, 1])
    sol.sortColors([0, 0])
