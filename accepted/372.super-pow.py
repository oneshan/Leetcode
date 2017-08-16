#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow
#
# Medium (33.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2\n[3]'
#
#
# Your task is to calculate ab mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
#
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
#
#
#
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.
#


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        for digit in b:
            ans = self.myPow(ans, 10) * self.myPow(a, digit) % 1337
        return ans

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x % 1337
        x %= 1337
        return self.myPow(x * x, n >> 1) * (1, x)[n & 1]


if __name__ == "__main__":
    sol = Solution()
    assert(sol.superPow(2, [1, 0]) == 1024)
