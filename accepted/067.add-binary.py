#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary
#
# Easy (31.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"0"\n"0"'
#
#
# Given two binary strings, return their sum (also a binary string).
#
#
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        if i < j:
            a, b, i, j = b, a, j, i

        ans, carry = "", 0

        while i >= 0 and j >= 0:
            num = int(a[i]) + int(b[j]) + carry
            carry = num >> 1
            ans = str(num & 1) + ans
            i -= 1
            j -= 1

        while i >= 0:
            num = int(a[i]) + carry
            carry = num >> 1
            ans = str(num & 1) + ans
            i -= 1

        if carry:
            ans = "1" + ans

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("1", "11"))
    print(sol.addBinary("1001", "101"))
