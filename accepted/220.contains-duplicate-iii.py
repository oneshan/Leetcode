#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii
#
# Medium (19.12%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]\n0\n0'
#
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
#
#


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        div = t + 1
        bucket = {}

        for idx, num in enumerate(nums):
            index = num // div
            for key in (index - 1, index, index + 1):
                if key in bucket and abs(bucket[key] - num) <= t:
                    return True
            bucket[index] = num
            if idx >= k:
                bucket.pop(nums[idx - k] // div)
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.containsNearbyAlmostDuplicate([10, 20, 30, 5], 3, 6) is True)
