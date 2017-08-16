#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square
#
# Easy (38.02%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
#
#
# Note: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
#
# Input: 16
# Returns: True
#
#
#
# Example 2:
#
# Input: 14
# Returns: False
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        left, right = 0, num - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = mid * mid
            if val == num:
                return True
            elif val < num:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isPerfectSquare(16) is True)
    assert(sol.isPerfectSquare(14) is False)
