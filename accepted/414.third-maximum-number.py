#
# [414] Third Maximum Number
#
# https://leetcode.com/problems/third-maximum-number
#
# Easy (27.74%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[3,2,1]'
#
# Given a non-empty array of integers, return the third maximum number in this
# array. If it does not exist, return the maximum number. The time complexity
# must be in O(n).
#
# Example 1:
#
# Input: [3, 2, 1]
#
# Output: 1
#
# Explanation: The third maximum is 1.
#
#
#
# Example 2:
#
# Input: [1, 2]
#
# Output: 2
#
# Explanation: The third maximum does not exist, so the maximum (2) is returned
# instead.
#
#
#
# Example 3:
#
# Input: [2, 2, 3, 1]
#
# Output: 1
#
# Explanation: Note that the third maximum here means the third maximum
# distinct number.
# Both numbers with value 2 are both considered as second maximum.
#
#
#


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        one = two = three = float('-inf')
        for num in nums:
            if num in (one, two, three):
                continue

            if num > one:
                one, two, three = num, one, two
            elif num > two:
                two, three = num, two
            elif num > three:
                three = num
        return three if three > float('-inf') else one


if __name__ == "__main__":
    sol = Solution()
    arr = [3, 2, 1]
    assert(sol.thirdMax(arr) == 1)
    arr = [1, 2]
    assert(sol.thirdMax(arr) == 2)
    arr = [2, 2, 3, 1]
    assert(sol.thirdMax(arr) == 1)
