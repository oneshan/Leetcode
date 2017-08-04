#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self
#
# Medium (48.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,0]'
#
# 
# Given an array of n integers where n > 1, nums, return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Solve it without division and in O(n).
# 
# For example, given [1,2,3,4], return [24,12,8,6].
# 
# Follow up:
# Could you solve it with constant space complexity? (Note: The output array
# does not count as extra space for the purpose of space complexity analysis.)
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1 for _ in range(len(nums))]
        p1 = p2 = 1

        for i in range(1, len(nums)):
            p1 *= nums[i - 1]
            p2 *= nums[-i]
            ans[i] *= p1
            ans[-i - 1] *= p2

        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4]
    assert(sol.productExceptSelf(arr) == [24, 12, 8, 6])
