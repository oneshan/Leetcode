#
# [78] Subsets
#
# https://leetcode.com/problems/subsets
#
# Medium (39.58%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
#
# Given a set of distinct integers, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,3], a solution is:
#
#
#
# [
# ⁠ [3],
# ⁠ [1],
# ⁠ [2],
# ⁠ [1,2,3],
# ⁠ [1,3],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ []
# ]
#
#


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            ans += [elem + [num] for elem in ans]
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
