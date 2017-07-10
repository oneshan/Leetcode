#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array
#
# Easy (31.91%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
#
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        if n > 0:
            nums1[:n] = nums2[:n]

        # print(nums1)

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 5, 0, 0, 0]
    nums2 = [3, 4, 5]
    m = n = 3
    sol.merge(nums1, m, nums2, n)
