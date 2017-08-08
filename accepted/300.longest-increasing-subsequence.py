#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence
#
# Medium (38.12%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
#
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is
# 4. Note that there may be more than one LIS combination, it is only necessary
# for you to return the length.
#
#
# Your algorithm should run in O(n2) complexity.
#
#
# Follow up: Could you improve it to O(n log n) time complexity? 
#
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = []
        for num in nums:
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if lis[mid] == num:
                    left = mid
                    break
                elif lis[mid] > num:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(lis):
                lis.append(num)
            else:
                lis[left] = num
        return len(lis)


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    assert(sol.lengthOfLIS(arr) == 4)
