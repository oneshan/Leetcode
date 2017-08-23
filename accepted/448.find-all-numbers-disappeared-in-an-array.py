#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
#
# Easy (51.94%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#
#


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        ans = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans += (i + 1),
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
