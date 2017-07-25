#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title
#
# Easy (25.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all
# test cases.
#


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans = ""
        while n:
            n -= 1
            n, r = n // 26, n % 26
            ans = mapping[r] + ans
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.convertToTitle(26))
    print(sol.convertToTitle(27))
