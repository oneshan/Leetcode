#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii
#
# algorithms
# Hard (32.19%)
# Total Accepted:    10.3K
# Total Submissions: 32.1K
# Testcase Example:  '"0"\n"0"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three
# strobogrammatic numbers.
#
#
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
#
#


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.ans = 0
        self.low, self.high = low, high
        for i in range(len(low), len(high) + 1):
            self.dfs(i, "")
        return self.ans

    def dfs(self, n, string):
        if n == 0:
            if len(self.low) == len(string) and self.low > string:
                return
            if len(self.high) == len(string) and self.high < string:
                return
            if len(string) == 1 or string[0] != '0':
                self.ans += 1
        elif n & 1:
            for ch in "018":
                self.dfs(n - 1, ch)
        else:
            for pair in ("11", "88", "00", "69", "96"):
                self.dfs(n - 2, pair[0] + string + pair[1])


if __name__ == "__main__":
    sol = Solution()
    assert(sol.strobogrammaticInRange("50", "100") == 3)
    assert(sol.strobogrammaticInRange("0", "0") == 1)
