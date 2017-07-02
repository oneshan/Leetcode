#
# [13] Roman to Integer
#
# https://leetcode.com/problems/roman-to-integer
#
# Easy (45.22%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"DCXXI"'
#
# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num, i, currV = 0, 1, roman[s[0]]
        while i < len(s):
            nextV = roman[s[i]]
            if nextV > currV:
                num -= currV
            else:
                num += currV
            i += 1
            currV = nextV
        num += currV
        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt('MCMLIV'))
    print(sol.romanToInt('MMXIV'))
