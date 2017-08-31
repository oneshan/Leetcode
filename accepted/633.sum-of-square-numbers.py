#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers
#
# Easy (31.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '5'
#
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
#
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
#
#
#
#
# Example 2:
#
# Input: 3
# Output: False
#
#
#
#


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        import math
        p1, p2 = 0, int(math.sqrt(c))
        while p1 <= p2:
            total = p1 * p1 + p2 * p2
            if total == c:
                return True
            elif total < c:
                p1 += 1
            else:
                p2 -= 1
        return False


if __name__ == "__main__":
    sol = Solution()
    assert(sol.judgeSquareSum(2) is True)
    assert(sol.judgeSquareSum(4) is True)
