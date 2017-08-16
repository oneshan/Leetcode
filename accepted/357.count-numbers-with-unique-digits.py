#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits
#
# Medium (45.84%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10n.
#
#
# ⁠   Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range
# of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans, count = 1, 9
        for i in range(min(n, 10)):
            ans += count
            count *= (9 - i)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.countNumbersWithUniqueDigits(1) == 10)
    assert(sol.countNumbersWithUniqueDigits(2) == 91)
