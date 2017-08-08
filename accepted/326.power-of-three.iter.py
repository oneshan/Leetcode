#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three
#
# Easy (40.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '27'
#
#
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
#
#
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        while n % 3 == 0:
            n /= 3
        return n == 1


if __name__ == "__main__":
    sol = Solution()
    assert(sol.isPowerOfThree(27) is True)
    assert(sol.isPowerOfThree(36) is False)
