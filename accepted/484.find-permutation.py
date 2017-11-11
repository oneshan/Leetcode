#
# [484] Find Permutation
#
# https://leetcode.com/problems/find-permutation
#
# algorithms
# Medium (55.10%)
# Total Accepted:    6.2K
# Total Submissions: 11.3K
# Testcase Example:  '"DDIIDI"'
#
#
# By now, you are given a secret signature consisting of character 'D' and 'I'.
# 'D' represents a decreasing relationship between two numbers, 'I' represents
# an increasing relationship between two numbers. And our secret signature was
# constructed by a special integer array, which contains uniquely all the
# different number from 1 to n (n is the length of the secret signature plus
# 1). For example, the secret signature "DI" can be constructed by array
# [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4],
# which are both illegal constructing special string that can't represent the
# "DI" secret signature.
#
#
#
# On the other hand, now your job is to find the lexicographically smallest
# permutation of [1, 2, ... n] could refer to the given secret signature in the
# input.
#
#
# Example 1:
#
# Input: "I"
# Output: [1,2]
# Explanation: [1,2] is the only legal initial spectial string can construct
# secret signature "I", where the number 1 and 2 construct an increasing
# relationship.
#
#
#
# Example 2:
#
# Input: "DI"
# Output: [2,1,3]
# Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature
# "DI", but since we want to find the one with the smallest lexicographical
# permutation, you need to output [2,1,3]
#
#
#
# Note:
# The input string will only contain the character 'D' and 'I'.
# The length of input string is a positive integer and will not exceed 10,000
#
#


class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        def reverse(i, j, arr):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        size = len(s)
        ans = [i for i in range(1, size + 2)]
        i = j = 0
        while i < size:
            if s[j] == 'D':
                while j < size and s[j] == 'D':
                    j += 1
                reverse(i, j, ans)
            i = j = j + 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert(sol.findPermutation("D") == [2, 1])
    assert(sol.findPermutation("DI") == [2, 1, 3])
    assert(sol.findPermutation("DDI") == [3, 2, 1, 4])
