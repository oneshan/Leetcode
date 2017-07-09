#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
#
# Medium (35.72%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
#
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
#
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i < 2 or num != nums[i - 2]:
                nums[i] = num
                i += 1
        return i

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, 5]
    print(sol.removeDuplicates(nums))
