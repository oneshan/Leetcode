#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii
#
# Easy (32.15%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0'
#
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
#
#


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for idx, num in enumerate(nums):
            if num in table and idx - table[num] <= k:
                return True
            table[num] = idx
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.containsNearbyDuplicate([1, 2, 3, 1], 1) is False)
    assert(sol.containsNearbyDuplicate([1, 2, 3, 1], 3) is True)
