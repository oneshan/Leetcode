#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive
#
# Hard (25.38%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given an unsorted integer array, find the first missing positive integer.
#
#
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
#
#
# Your algorithm should run in O(n) time and uses constant space.
#
#


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums += 0,
        size = len(nums)
        for i in range(size):
            while size > nums[i] >= 0 and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]

        for i in range(1, size):
            if nums[i] != i:
                return i
        return size

if __name__ == "__main__":
    sol = Solution()
    arr = [3, 4, -1, 1]
    print(sol.firstMissingPositive(arr))

    arr = [1, 2, 10]
    print(sol.firstMissingPositive(arr))

    arr = [1, 2, 0]
    print(sol.firstMissingPositive(arr))

    arr = []
    print(sol.firstMissingPositive(arr))

    arr = [1]
    print(sol.firstMissingPositive(arr))

    arr = [2]
    print(sol.firstMissingPositive(arr))
