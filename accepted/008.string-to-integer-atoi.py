#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi
#
# Medium (13.94%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases. If you want a challenge,
# please do not see below and ask yourself what are the possible input cases.
#
#
# Notes: 
# It is intended for this problem to be specified vaguely (ie, no given input
# specs). You are responsible to gather all the input requirements up front. 
#
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button  to reset your code definition.
#
#
# spoilers alert... click to show requirements for atoi.
#
# Requirements for atoi:
#
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
#
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned. If the
# correct value is out of the range of representable values, INT_MAX
# (2147483647) or INT_MIN (-2147483648) is returned.
#
#
#
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # strip spaces
        idx = 0
        while idx < len(str) and str[idx] == " ":
            idx += 1

        # Check empty string
        if idx == len(str):
            return 0

        # negative number
        sign = 1
        if str[idx] == '-':
            sign = -1
            idx += 1
        elif str[idx] == '+':
            sign = 1
            idx += 1

        # str to int
        num = 0
        while idx < len(str):
            val = ord(str[idx]) - 48
            if val < 0 or val > 9:
                break
            num = num * 10 + val
            idx += 1
        num *= sign

        # Check overflow
        return max(-2147483648, (min(2147483647, num)))


if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi(' -2'))
    print(sol.myAtoi(' 123a'))
    print(sol.myAtoi('123'))
    print(sol.myAtoi('+123'))
