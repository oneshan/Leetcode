#
# [658] Find K Closest Elements
#
# https://leetcode.com/problems/find-k-closest-elements
#
# Medium (35.89%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
#
# Given a sorted array, two integers k and x, find the k closest elements to x
# in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
#
#
# Example 1:
#
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
#
#
#
#
# Example 2:
#
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
#
#
#
# Note:
#
# The value k is positive and will always be smaller than the length of the
# sorted array.
# ⁠Length of the given array is positive and will not exceed 104
# ⁠Absolute value of elements in the array and x will not exceed 104
#
#
#


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > x:
                right = mid - 1
            elif arr[mid] < x:
                left = mid + 1
            else:
                left = mid
                break

        p1 = p2 = left
        while p2 - p1 <= k:
            if p1 <= 0:
                return arr[:k]
            if p2 == len(arr):
                return arr[-k:]
            if x - arr[p1] <= arr[p2] - x:
                p1 -= 1
            else:
                p2 += 1

        return arr[p1 + 1:p2]


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    assert(sol.findClosestElements(arr, 4, 3) == [1, 2, 3, 4])
    arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    assert(sol.findClosestElements(arr, 3, 5) == [3, 3, 4])
    arr = [1, 1, 2, 3, 3, 3, 4, 6, 8, 8]
    assert(sol.findClosestElements(arr, 6, 1) == [1, 1, 2, 3, 3, 3])
