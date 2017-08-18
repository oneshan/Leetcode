#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#
# Medium (32.78%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n5'
#
#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.
#


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == nums[right] == target:
                return True
            while left <= right and nums[left] == nums[right]:
                right -= 1

            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.search([1, 1, 2, 3, 4, 5, 1, 1], 3) is True)
