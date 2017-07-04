#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position
#
# Easy (39.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n0'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
#
# You may assume no duplicates in the array.
#
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0
#
#


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    sol = Solution()

    arr = []
    target = 8
    print(arr, target, sol.searchInsert(arr, target))

    arr = [1, 3, 5]
    target = 1
    print(arr, target, sol.searchInsert(arr, target))

    arr = [1, 3, 5]
    target = 0
    print(arr, target, sol.searchInsert(arr, target))

    arr = [1, 3, 5]
    target = 2
    print(arr, target, sol.searchInsert(arr, target))

    arr = [1, 3, 5]
    target = 6
    print(arr, target, sol.searchInsert(arr, target))
