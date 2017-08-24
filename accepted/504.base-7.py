#
# [504] Base 7
#
# https://leetcode.com/problems/base-7
#
# Easy (44.87%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#
#


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        isNeg = num < 0
        num = abs(num)
        
        ans = ""
        while num:
            ans = str(num % 7) + ans
            num //= 7
        
        return ("", "-")[isNeg] + ans if ans else "0"


if __name__ == "__main__":
    sol = Solution()
    assert(sol.convertToBase7(-7) == "-10")
    assert(sol.convertToBase7(100) == "202")
