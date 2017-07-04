#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation
#
# Medium (28.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
#
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
#
#
# The replacement must be in-place, do not allocate extra memory.
#
#
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # From right to left, find non-increasing suffix
        j = len(nums) - 1
        while j > 0 and nums[j] <= nums[j - 1]:
            j -= 1

        if j > 0:
            # Find successor to the change number
            i = len(nums) - 1
            while i >= j and nums[i] <= nums[j - 1]:
                i -= 1
            # Swap two element
            nums[i], nums[j - 1] = nums[j - 1], nums[i]

        # Reverse from j to the end
        nums[j:] = nums[j:][::-1]

        print(nums)

if __name__ == "__main__":
    sol = Solution()
    nums = [5, 4, 3, 2, 1]
    sol.nextPermutation(nums)
    nums = [4, 7, 5, 3, 1]
    sol.nextPermutation(nums)
