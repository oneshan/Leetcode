#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays
#
# Hard (21.46%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        k = len(nums1) + len(nums2)
        if k & 1:
            return self.recur(nums1, nums2, k // 2 + 1)
        else:
            n1 = self.recur(nums1, nums2, k // 2)
            n2 = self.recur(nums1, nums2, k // 2 + 1)
            return (n1 + n2) * 1.0 / 2

    def recur(self, nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]
        if not nums2:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])

        isOdd, k = k & 1, k // 2
        n1 = nums1[k - 1] if len(nums1) >= k else float('inf')
        n2 = nums2[k - 1] if len(nums2) >= k else float('inf')
        if n1 < n2:
            return self.recur(nums1[k:], nums2, k + isOdd)
        return self.recur(nums1, nums2[k:], k + isOdd)
