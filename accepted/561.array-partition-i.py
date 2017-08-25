#
# [561] Array Partition I
#
# https://leetcode.com/problems/array-partition-i
#
# Easy (68.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,4,3,2]'
#
#
# Given an array of 2n integers, your task is to group these integers into n
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
# min(ai, bi) for all i from 1 to n as large as possible.
#
#
# Example 1:
#
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3,
# 4).
#
#
#
# Note:
#
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
#
#
#


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = [0] * 20001
        for num in nums:
            table[num + 10000] += 1

        odd = True
        ans = -10000 * (len(nums) >> 1)
        for i in range(20001):
            while table[i] > 0:
                if odd:
                    ans += i
                table[i] -= 1
                odd ^= True
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.arrayPairSum([1, 4, 3, 2]) == 4)
