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

        nums1.sort()
        nums2.sort()
        ans = []

        p1 = p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.intersect([1, 2, 2, 1], [2, 2]) == [2, 2])
