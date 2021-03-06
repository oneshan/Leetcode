#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number
#
# Easy (46.69%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"A"'
#
# Related to question Excel Sheet Column Title
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        table = dict((ch, idx) for idx, ch in enumerate(mapping, 1))
        num = 0
        for ch in s:
            num = num * 26 + table[ch]
        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("Z"))
    print(sol.titleToNumber("AA"))
    print(sol.titleToNumber("AB"))
