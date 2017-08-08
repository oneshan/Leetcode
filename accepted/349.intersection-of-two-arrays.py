#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays
#
# Easy (47.00%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n[]'
#
#
# Given two arrays, write a function to compute their intersection.
#
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
#
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.
#
#
#


class Solution(object):
    def intersection(self, nums1, nums2):
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
                if not ans or nums1[p1] != ans[-1]:
                    ans.append(nums1[p1])
                p1 += 1
                p2 += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.intersection([1, 2, 2, 1], [2, 2]) == [2])
