#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii
#
# Medium (32.32%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,1,2]'
#
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
#
#
#
# For example,
# [1,1,2] have the following unique permutations:
#
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#
#


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        nums.sort()
        self.dfs([], nums)
        return self.ans

    def dfs(self, arr, remains):
        if not remains:
            self.ans += arr,
        for idx, elem in enumerate(remains):
            # skip duplicate
            if idx and remains[idx] == remains[idx - 1]:
                continue
            self.dfs(arr + [elem], remains[:idx] + remains[idx + 1:])


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2]
    print(sol.permuteUnique(arr))
