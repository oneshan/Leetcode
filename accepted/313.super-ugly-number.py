#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number
#
# Medium (37.49%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n[2,3,5]'
#
#
# ⁠   Write a program to find the nth super ugly number.
#
#
#
# ⁠   Super ugly numbers are positive numbers whose all prime factors are in
# the given prime list
# ⁠   primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28,
# 32]
# ⁠is the sequence of the first 12 super ugly numbers given primes
# ⁠   = [2, 7, 13, 19] of size 4.
#
#
#
# ⁠   Note:
# ⁠   (1) 1 is a super ugly number for any given primes.
# ⁠   (2) The given numbers in primes are in ascending order.
# ⁠   (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# ⁠   (4) The nth super ugly number is guaranteed to fit in a 32-bit signed
# integer.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        ptr = {prime: 0 for prime in primes}
        for _ in range(n - 1):
            nextUgly = float('inf')
            for prime in primes:
                if ugly[ptr[prime]] * prime <= ugly[-1]:
                    ptr[prime] += 1
                nextUgly = min(nextUgly, ugly[ptr[prime]] * prime)
            ugly.append(nextUgly)
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    primes = [2, 7, 13, 19]
    assert(sol.nthSuperUglyNumber(12, primes) == 32)
