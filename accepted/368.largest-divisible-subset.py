#
# [368] Largest Divisible Subset
#
# https://leetcode.com/problems/largest-divisible-subset
#
# Medium (33.64%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
#
# Given a set of distinct positive integers, find the largest subset such that
# every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj %
# Si = 0.
#
#
# If there are multiple solutions, return any subset is fine.
#
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)
        dp = [(1, -1) for _ in range(n)]
        maxLen, maxIndex = 0, -1

        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j][0] > dp[i][0]:
                        dp[i] = (dp[j][0] + 1, j)

            if dp[i][0] >= maxLen:
                maxLen, maxIndex = dp[i][0], i

        ans = []
        for _ in range(maxLen):
            ans += nums[maxIndex],
            maxIndex = dp[maxIndex][1]

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sorted(sol.largestDivisibleSubset([1, 2, 3])) == [1, 3])
    assert(sorted(sol.largestDivisibleSubset([1, 2, 4, 8])) == [1, 2, 4, 8])
