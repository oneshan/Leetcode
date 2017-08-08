#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap
#
# Hard (29.30%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
#
# Credits:Special thanks to @porker2008 for adding this problem and creating
# all test cases.
#


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        maxV = max(nums)
        minV = min(nums)
        b_size = (maxV - minV) // n + 1
        b_num = (maxV - minV) // b_size + 1
        bucket = [None for _ in range(b_num)]

        for num in nums:
            index = (num - minV) // b_size
            if not bucket[index]:
                bucket[index] = [num, num]
            else:
                bucket[index][0] = min(bucket[index][0], num)
                bucket[index][1] = max(bucket[index][1], num)

        gap = prev = 0
        for i in range(1, b_num):
            if not bucket[i]:
                continue
            gap = max(gap, bucket[i][0] - bucket[prev][1])
            prev = i

        return gap


if __name__ == "__main__":
    sol = Solution()
    assert(sol.maximumGap([1, 3, 5, 7, 10]) == 3)
    assert(sol.maximumGap([3, 6, 9, 1]) == 3)
