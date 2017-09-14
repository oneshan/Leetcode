#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number
#
# Hard (12.70%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"3"'
#
# Validate if a given string is numeric.
#
#
# Some examples:
# "0" => true
# "   0.1  " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
#
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one.
#
#
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button  to reset your code definition.
#
#


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        p1, p2 = 0, len(s) - 1
        number = "0123456789"

        # space clear
        while p1 < p2 and s[p1] == ' ':
            p1 += 1
        while p1 < p2 and s[p2] == ' ':
            p2 -= 1
        if s[p1] in '+-':
            p1 += 1

        isNum = isDot = isExp = False
        while p1 <= p2:
            if s[p1] in number:
                p1 += 1
                isNum = True
            elif s[p1] == '.' and not isDot and not isExp:
                p1 += 1
                isDot = True
            elif s[p1] == 'e' and not isExp and isNum:
                p1 += 1
                if p1 <= p2 and s[p1] in '+-':
                    p1 += 1
                isExp = True
                isNum = False
            else:
                return False
        return isNum


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isNumber("0") is True)
    assert(sol.isNumber("    0.1   ") is True)
    assert(sol.isNumber("2e10") is True)

    assert(sol.isNumber("abc") is False)
    assert(sol.isNumber("1 a") is False)
    assert(sol.isNumber(" -.") is False)

    assert(sol.isNumber("e10") is False)
    assert(sol.isNumber("0e") is False)
    assert(sol.isNumber("1e") is False)
    assert(sol.isNumber("1e.") is False)
    assert(sol.isNumber("1.") is True)
    assert(sol.isNumber("-1.") is True)
    assert(sol.isNumber("+.8") is True)
    assert(sol.isNumber("0e1") is True)
    assert(sol.isNumber("46.e3") is True)
    assert(sol.isNumber(".e1") is False)
    assert(sol.isNumber("6e6.5") is False)
    assert(sol.isNumber(" 005047e+6") is True)
