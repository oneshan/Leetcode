#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers
#
# Medium (15.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0\n1'
#
#
# Divide two integers without using multiplication, division and mod
# operator.
#
#
# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Store numbers' sign
        sign = 1 if (dividend ^ divisor) >= 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        return min(max(-2147483648, res * sign), 2147483647)


if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(12340, 4))
    print(sol.divide(12340, -4))
    print(sol.divide(-12340, -4))
    print(sol.divide(2147483648, 1))
    print(sol.divide(1, 1))
