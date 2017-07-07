#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one
#
# Easy (38.27%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
# Given a non-negative integer represented as a non-empty array of digits, plus
# one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number
# 0 itself.
#
# The digits are stored such that the most significant digit is at the head of
# the list.
#


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        j = len(digits) - 1
        while j >= 0:
            if digits[j] == 9:
                digits[j] = 0
                j -= 1
            else:
                digits[j] += 1
                break
        else:
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    sol = Solution()
    digits = [9, 9, 9]
    print(sol.plusOne(digits))
    digits = []
    print(sol.plusOne(digits))
