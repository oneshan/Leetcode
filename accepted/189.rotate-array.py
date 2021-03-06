#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array
#
# Easy (24.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n0'
#
# Rotate an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
# [5,6,7,1,2,3,4]. 
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
#
#
# [show hint]
# Hint:
# Could you do it in-place with O(1) extra space?
#
#
# Related problem: Reverse Words in a String II
#
# Credits:Special thanks to @Freezen for adding this problem and creating all
# test cases.
#


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        reverse(0, n - k - 1)
        reverse(n - k, n - 1)
        reverse(0, n - 1)
        """
        for i in range(k):
            temp = nums[-1]
            for j in range(1, len(nums)):
                nums[-j] = nums[-j - 1]
            nums[0] = temp
        """
        print(nums)


if __name__ == "__main__":
    sol = Solution()
    sol.rotate([1, 2, 3, 4, 5, 6, 7], 3)
