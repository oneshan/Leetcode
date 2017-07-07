#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx
#
# Easy (27.64%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, (x + 1) >> 1
        while left <= right:
            mid = left + (right - left) // 2
            value = mid * mid
            if value == x:
                return mid
            elif value > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(0))
    print(sol.mySqrt(1))
    print(sol.mySqrt(30))
