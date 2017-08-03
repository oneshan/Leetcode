#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii
#
# Medium (28.43%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n1, n2, count1, count2 = None, None, 0, 0
        for num in nums:
            if n1 == num:
                count1 += 1
            elif n2 == num:
                count2 += 1
            elif count1 == 0:
                n1, count1 = num, 1
            elif count2 == 0:
                n2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if n1 == num:
                count1 += 1
            elif n2 == num:
                count2 += 1

        ans = []
        if count1 > len(nums) // 3:
            ans += n1,
        if count2 > len(nums) // 3:
            ans += n2,
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.majorityElement([1, 1, 2, 2, 3]) == [1, 2])
    assert(sol.majorityElement([1, 1, 1, 1, 2]) == [1])
    assert(sol.majorityElement([1, 2, 3, 4, 5]) == [])
