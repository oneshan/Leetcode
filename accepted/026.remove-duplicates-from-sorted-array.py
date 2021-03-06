#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
#
# Easy (35.54%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a sorted array, remove the duplicates in place such that each element
# appear only once and return the new length.
#
#
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
#
#
#
# For example,
# Given input array nums = [1,1,2],
#
#
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively. It doesn't matter what you leave beyond the new
# length.
#
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        idx = 0
        for num in nums:
            if nums[idx] == num:
                continue
            idx += 1
            nums[idx] = num

        return idx + 1


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 1, 3, 4, 4, 5]
    print(sol.removeDuplicates(arr))
