#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four
#
# Easy (38.28%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '16'
#
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num & (num - 1):
            return False
        if num & 0xAAAAAAAA:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isPowerOfFour(64) is True)
    assert(sol.isPowerOfFour(24) is False)
