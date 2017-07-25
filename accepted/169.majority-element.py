#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element
#
# Easy (46.23%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, count = nums[0], 0

        for num in nums:
            if count == 0:
                ans, count = num, 1
            elif num == ans:
                count += 1
            else:
                count -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([1, 2, 2, 3]))
    print(sol.majorityElement([1, 1, 2, 3, 3, 1, 1]))
    print(sol.majorityElement([1, 1, 2, 2, 3, 3, 3]))
