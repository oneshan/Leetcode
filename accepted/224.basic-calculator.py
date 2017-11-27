#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator
#
# Hard (26.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#
#
#
#
# Note: Do not use the eval built-in library function.
#
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = ''
        ans = [[0]]
        count = 0
        for ch in s[::-1]:

            if ch == ' ':
                continue
            elif ch in '0123456789':
                num = ch + num
            elif num:
                ans[-1].append(int(num))
                num = ''
                count += 1
 
            if ch == '-':
                ans[-1][-1] *= -1
            elif ch == ')':
                ans.append([])
            elif ch == '(':
                val = sum(ans.pop())
                ans[-1].append(val)

        if num:
            ans[-1].append(int(num))

        return sum(ans[-1])
