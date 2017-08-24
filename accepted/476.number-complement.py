#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement
#
# Easy (61.37%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
#
# Note:
#
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
#
#
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
#
#
#
# Example 2:
#
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
#
#
#


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        power2 = 1
        while power2 <= num:
            power2 <<= 1
        
        return num ^ (power2 - 1)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findComplement(1) == 0)
    assert(sol.findComplement(5) == 2)
