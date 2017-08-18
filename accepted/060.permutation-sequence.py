#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence
#
# Medium (28.13%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1\n1'
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
#
# Given n and k, return the kth permutation sequence.
#
# Note: Given n will be between 1 and 9 inclusive.
#


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        fact = [1 for _ in range(n)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        ans = ""
        for i in range(n - 1, -1, -1):
            j = 0
            while k > fact[i]:
                k -= fact[i]
                j += 1
            ans += str(nums[j])
            nums.remove(nums[j])

        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.getPermutation(3, 3) == "213")
