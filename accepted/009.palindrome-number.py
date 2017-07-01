#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number
#
# Easy (35.01%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '-2147483648'
#
# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
#
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction
# of using extra space.
#
# You could also try reversing an integer. However, if you have solved the
# problem "Reverse Integer", you know that the reversed integer might overflow.
# How would you handle such case?
#
# There is a more generic way of solving this problem.
#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        rev, temp = 0, x
        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10

        return rev == x


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(12345))
    print(sol.isPalindrome(1))
    print(sol.isPalindrome(121))
