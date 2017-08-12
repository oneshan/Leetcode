#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number
#
# Easy (33.56%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
#
#
# Example:
#
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
#
#
#
# Note:
# The input number n will not exceed 100,000,000. (1e8)
#
#


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False

        i, total = 2, 1
        while i * i < num:
            if num % i == 0:
                total += i + num // i
            i += 1
        return total == num


if __name__ == "__main__":
    sol = Solution()
    assert(sol.checkPerfectNumber(28) is True)
