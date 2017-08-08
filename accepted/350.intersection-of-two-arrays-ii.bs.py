#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii
#
# Easy (44.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
#
# Given two arrays, write a function to compute their intersection.
#
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
#
# Note:
#
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
#
#
#
# Follow up:
#
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
#
#
#


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        nums1.sort()
        nums2.sort()
        ans = []

        left = 0
        for num in nums1:
            right = len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if num > nums2[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left < len(nums2) and nums2[left] == num:
                ans += num,
                left += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.intersect([1, 2, 2, 1], [2, 2]) == [2, 2])
