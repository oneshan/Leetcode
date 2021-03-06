#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses
#
# Easy (33.20%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"["'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid
# but "(]" and "([)]" are not.
#


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for ch in s:
            if ch in '({[':
                stack += ch,
            elif not stack:
                return False
            else:
                pre = stack.pop()
                if ch == ')' and pre != '(':
                    return False
                elif ch == '}' and pre != '{':
                    return False
                elif ch == ']' and pre != '[':
                    return False
        if stack:
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid('('))
    print(sol.isValid('()[]{}'))
    print(sol.isValid('({[]})'))
    print(sol.isValid('({)'))
