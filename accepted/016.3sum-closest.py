#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest
#
# Medium (30.94%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0,0,0]\n1'
#
# Given an array S of n integers, find three integers in S such that the sum is
# closest to a given number, target. Return the sum of the three integers. You
# may assume that each input would have exactly one solution.
#
#
# ⁠   For example, given array S = {-1 2 1 -4}, and target = 1.
#
# ⁠   The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans, minDiff = 0, float('inf')
        n = len(nums)

        nums.sort()
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # find the closest sum
                diff = abs(target - total)
                if diff < minDiff:
                    ans, minDiff = total, diff

                # update pointer
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    return target

        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [-1, 2, 1, -4]
    target = 1
    print(sol.threeSumClosest(arr, target))
