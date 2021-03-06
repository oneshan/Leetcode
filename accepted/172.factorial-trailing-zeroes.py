#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes
#
# Easy (35.73%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        five = 5
        ans = 0
        while five <= n:
            ans += n // five
            five *= 5
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(10))
    print(sol.trailingZeroes(25))
