#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range
#
# Medium (31.26%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers sorted in ascending order, find the starting and
# ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#
#


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Find the target
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:   # target not found
            return [-1, -1]

        ans = [mid, mid]

        # Find left boundary
        left, right = 0, ans[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        ans[0] = left

        # Find right boundary
        left, right = ans[1], len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        ans[1] = right

        return ans

if __name__ == "__main__":
    sol = Solution()

    arr = []
    target = 8
    print(arr, target, sol.searchRange(arr, target))

    arr = [2, 2]
    target = 3
    print(arr, target, sol.searchRange(arr, target))

    arr = [1, 2, 3]
    target = 2
    print(arr, target, sol.searchRange(arr, target))

    arr = [5, 7, 7, 8, 8, 8, 8, 8, 10]
    target = 8
    print(arr, target, sol.searchRange(arr, target))

    arr = [5, 7, 7, 8, 8, 8, 11, 12, 13]
    target = 8
    print(arr, target, sol.searchRange(arr, target))

    arr = [5, 7, 7, 8, 8, 10]
    target = 6
    print(arr, target, sol.searchRange(arr, target))
