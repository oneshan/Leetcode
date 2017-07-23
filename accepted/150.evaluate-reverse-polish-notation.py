#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation
#
# Medium (26.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["18"]'
#
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#
#
# Valid operators are +, -, *, /. Each operand may be an integer or another
# expression.
#
#
#
# Some examples:
#
# ⁠ ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ⁠ ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
#
#


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0

        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif num1 ^ num2 >= 0:
                    stack.append(num1 // num2)
                else:   # Note: In Python3, -1 // 2 == -1
                    stack.append(-(abs(num1) // abs(num2)))
        return stack[-1]


if __name__ == "__main__":
    sol = Solution()
    arr = ["2", "1", "+", "3", "*"]
    print(sol.evalRPN(arr))
    arr = ["4", "13", "5", "/", "+"]
    print(sol.evalRPN(arr))
    arr = ["18"]
    print(sol.evalRPN(arr))
    arr = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(sol.evalRPN(arr))
