#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array
#
# Medium (54.82%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#
#


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums += [0]
        nums[0], nums[-1] = nums[-1], nums[0]

        for i in range(1, len(nums)):
            j = nums[i]
            while nums[i] != i and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i]

        ans = []
        for idx, num in enumerate(nums):
            if idx != num:
                ans.append(num)

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3])
