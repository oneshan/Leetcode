#
# [77] Combinations
#
# https://leetcode.com/problems/combinations
#
# Medium (39.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '4\n2'
#
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
#
# For example,
# If n = 4 and k = 2, a solution is:
#
#
#
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]

        ans = [r + [n] for r in self.combine(n - 1, k - 1)]
        if n > k:
            ans += self.combine(n - 1, k)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.combine(4, 2))
