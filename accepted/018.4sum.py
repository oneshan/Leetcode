#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum
#
# Medium (26.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array S of n integers, are there elements a, b, c, and d in S such
# that a + b + c + d = target? Find all unique quadruplets in the array which
# gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
#
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n - 3):
            # Skip duplicate
            if a and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, n - 2):
                # Skip duplicate
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c, d = b + 1, n - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total > target:
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        ans += [nums[a], nums[b], nums[c], nums[d]],
                        d -= 1
                        c += 1
                        # Skip duplicate
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.fourSum(arr, target))

    arr = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(sol.fourSum(arr, target))

