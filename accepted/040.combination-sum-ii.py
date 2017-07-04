#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii
#
# Medium (33.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
#
# Given a collection of candidate numbers (C) and a target number (T), find all
# unique combinations in C where the candidate numbers sums to T.
#
#
# Each number in C may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
#
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.ans = []
        self.search(candidates, target, [], 0)
        return self.ans

    def search(self, candidates, target, arr, idx):
        if target == 0:
            self.ans += arr,
        for i in range(idx, len(candidates)):
            value = target - candidates[i]
            # skip duplicate combinations
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            if value >= 0:
                # Since candidates[i] only be used once, idx = i + 1
                self.search(candidates, value, arr + [candidates[i]], i + 1)


if __name__ == "__main__":
    sol = Solution()
    candidates = []
    target = 7
    print(sol.combinationSum2(candidates, target))

    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum2(candidates, target))

    candidates = [2, 2, 2, 3, 6, 7]
    target = 7
    print(sol.combinationSum2(candidates, target))
