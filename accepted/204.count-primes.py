#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes
#
# Easy (26.45%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '0'
#
# Description:
# Count the number of prime numbers less than a non-negative number, n.
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all
# test cases.
#


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        isPrime = [1 for _ in range(n)]
        isPrime[0] = isPrime[1] = 0

        for i in range(2, n):
            if not isPrime[i]:
                continue
            curr = i + i
            while curr < n:
                isPrime[curr] = 0
                curr += i
        return sum(isPrime)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countPrimes(2))
    print(sol.countPrimes(3))
    print(sol.countPrimes(10))
