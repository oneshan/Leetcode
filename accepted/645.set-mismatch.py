#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch
#
# Easy (40.53%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,2,4]'
#
#
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
#
#
#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
#
#
# Note:
#
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
#
#
#


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.append(0)
        nums[-1], nums[0] = nums[0], nums[-1]

        n = len(nums)
        ans = [-1, -1]

        for i in range(n):
            val = abs(nums[i])
            if nums[val] < 0:
                ans[0] = val
            else:
                nums[val] *= -1

        for i in range(n):
            if nums[i] > 0:
                ans[1] = i
                break

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findErrorNums([1, 2, 2, 4]) == [2, 3])
