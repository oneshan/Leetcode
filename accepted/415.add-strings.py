#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings
#
# Easy (41.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
#
#
#


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return num1 + num2

        n1, n2 = len(num1), len(num2)
        idx = max(n1, n2)

        ans = ""
        num = 0
        for i in range(idx):
            if i < n1:
                num += int(num1[-1 - i])
            if i < n2:
                num += int(num2[-1 - i])
            ans = str(num % 10) + ans
            num //= 10

        if num:
            ans = str(num % 10) + ans

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.addStrings("123", "99") == "222")
