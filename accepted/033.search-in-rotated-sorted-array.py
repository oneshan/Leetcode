#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array
#
# Medium (32.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n5'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        # Find the rotated pivot
        left, right, pivot = 0, len(nums) - 1, None
        while left < right:
            mid = left + (right - left) // 2
            if mid < right and nums[mid] > nums[mid + 1]:
                pivot = mid
                break
            if mid > left and nums[mid] < nums[mid - 1]:
                pivot = mid - 1
                break
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            pivot = len(nums) - 1

        # Find the target
        if target == nums[0]:
            return 0
        elif target > nums[0]:
            left, right = 1, pivot
        else:
            left, right = pivot + 1, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


if __name__ == "__main__":
    sol = Solution()

    arr = []
    target = 5
    print(arr, target, sol.search(arr, target))

    arr = [0, 1, 2, 4, 5, 6, 7]
    target = 4
    print(arr, target, sol.search(arr, target))

    arr = [2, 4, 5, 6, 7, 0, 1]
    target = 2
    print(arr, target, sol.search(arr, target))

    arr = [2, 4, 5, 6, 7, 0, 1]
    target = 3
    print(arr, target, sol.search(arr, target))

    arr = [2, 4, 5, 6, 7, 0, 1]
    target = 4
    print(arr, target, sol.search(arr, target))
