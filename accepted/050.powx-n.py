#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n
#
# Medium (26.48%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '8.88023\n3'
#
# Implement pow(x, n).


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == -1:
            return 1 / x
        return self.myPow(x * x, n >> 1) * (1, x)[n & 1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(8.88023, 3))
