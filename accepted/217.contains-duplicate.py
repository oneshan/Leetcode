#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate
#
# Easy (45.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given an array of integers, find if the array contains any duplicates. Your
# function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
#
#


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.containsDuplicate([1, 2, 3]) is False)
    assert(sol.containsDuplicate([1, 2, 3, 3]) is True)
