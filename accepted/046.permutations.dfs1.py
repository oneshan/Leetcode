#
# [46] Permutations
#
# https://leetcode.com/problems/permutations
#
# Medium (42.93%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
#
# Given a collection of distinct numbers, return all possible permutations.
#
#
#
# For example,
# [1,2,3] have the following permutations:
#
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.dfs([], nums)
        return self.ans

    def dfs(self, arr, remains):
        if not remains:
            self.ans += arr,
        for idx, elem in enumerate(remains):
            self.dfs(arr + [elem], remains[:idx] + remains[idx + 1:])

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3]
    print(sol.permute(arr))
