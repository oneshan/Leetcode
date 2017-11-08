#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii
#
# algorithms
# Medium (40.39%)
# Total Accepted:    24K
# Total Submissions: 59.3K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n. 
# For example,
# Given n = 2, return ["11","69","88","96"].
#
#


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.dfs(n, "")
        return self.ans
    
    def dfs(self, n, string):
        if n == 0:
            if len(string) == 1 or string[0] != '0':
                self.ans.append(string)
        elif n & 1:
            for ch in "018":
                self.dfs(n - 1, ch)
        else:
            for pair in ("11", "88", "00", "69", "96"):
                self.dfs(n - 2, pair[0] + string + pair[1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.findStrobogrammatic(1))
    print(sol.findStrobogrammatic(2))
    print(sol.findStrobogrammatic(3))

