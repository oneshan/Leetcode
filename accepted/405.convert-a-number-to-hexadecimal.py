#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal
#
# Easy (40.98%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '26'
#
#
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#
#
#


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += (1 << 32)

        mapping = "0123456789abcdef"
        ans = ""
        while num:
            ans = mapping[num % 16] + ans
            num >>= 4
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.toHex(16) == "10")
    assert(sol.toHex(-1) == "ffffffff")
