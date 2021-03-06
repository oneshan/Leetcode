#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number
#
# Medium (43.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1]'
#
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
#
#
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                return slow


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findDuplicate([1, 1]) == 1)
    assert(sol.findDuplicate([1, 2, 3, 4, 3]) == 3)
