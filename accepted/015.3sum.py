#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum
#
# Medium (21.55%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array S of n integers, are there elements a, b, c in S such that a +
# b + c = 0? Find all unique triplets in the array which gives the sum of
# zero.
#
# Note: The solution set must not contain duplicate triplets.
#
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n - 2):
            # Skip duplicate case
            if i and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate case
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(arr))
    arr = [0, 0, 0]
    print(sol.threeSum(arr))
