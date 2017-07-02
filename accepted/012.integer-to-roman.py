#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman
#
# Medium (44.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Given an integer, convert it to a roman numeral.
#
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        numerals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        ans = ""
        for numeral, roman in zip(numerals, romans):
            while num >= numeral:
                ans += roman
                num -= numeral
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3999))
    print(sol.intToRoman(444))
    print(sol.intToRoman(1234))
