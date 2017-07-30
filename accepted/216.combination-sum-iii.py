#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii
#
# Medium (44.36%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '3\n7'
#
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
#
#
#
# ⁠Example 1:
# Input:  k = 3,  n = 7
# Output: 
#
# [[1,2,4]]
#
#
# ⁠Example 2:
# Input:  k = 3,  n = 9
# Output: 
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
#
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.ans = []
        self.recur([], k, n, 0)
        return self.ans

    def recur(self, arr, k, n, idx):
        if n < 0:
            return
        if k == 0:
            if n == 0:
                self.ans += arr,
            return

        for i in range(idx + 1, 10):
            self.recur(arr + [i], k - 1, n - i, i)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
