#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii
#
# Medium (35.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,2]'
#
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,2], a solution is:
#
#
#
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        nums.sort()
        self.result = []
        n = len(nums)

        def recur(arr, idx):
            self.result += arr,
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                recur(arr + [nums[i]], i + 1)

        recur([], 0)
        return self.result


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 2]
    print(sol.subsetsWithDup(arr))
