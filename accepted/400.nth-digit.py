#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit
#
# Easy (30.14%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#
#
#


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, count = 1, 9
        while  n > base * count:
            n -= base * count
            count *= 10
            base += 1

        num = str(pow(10, base - 1) + (n - 1) // base)
        return int(num[(n - 1) % base])


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findNthDigit(11) == 0)
