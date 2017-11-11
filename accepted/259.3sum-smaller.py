#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller
#
# algorithms
# Medium (41.64%)
# Total Accepted:    29.6K
# Total Submissions: 71.2K
# Testcase Example:  '[]\n0'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2:
#
# [-2, 0, 1]
# [-2, 0, 3]
#
#
# Follow up:
# Could you solve it in O(n2) runtime?
#
#


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum >= target:
                    k -= 1
                else:
                    ans += k - j
                    j += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert(sol.threeSumSmaller([-2, 0, 1, 3], 2) == 2)
