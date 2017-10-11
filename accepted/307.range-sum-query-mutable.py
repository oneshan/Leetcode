# -*- coding: utf-8 -*-
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable
#
# Medium (20.10%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i
# to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
#
#
#
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
#
#
#


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.size = len(nums) + 1
        self.nums = [0] * (self.size - 1)
        self.tree = [0] * self.size
        for i, val in enumerate(nums):
            self.update(i, val)

    def _update(self, i, delta):
        while i < self.size:
            self.tree[i] += delta
            i += i & (-i)

    def _sum(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & (-i)
        return ans

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        delta = val - self.nums[i]
        self.nums[i] = val
        self._update(i + 1, delta)
    
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._sum(j + 1) - self._sum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
if __name__ == "__main__":
    nums = [1, 3, 5]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))
    obj.update(1, 2)
    print(obj.sumRange(0, 2))
