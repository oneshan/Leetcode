#
# [683] K Empty Slots
#
# https://leetcode.com/problems/k-empty-slots
#
# algorithms
# Hard (36.69%)
# Total Accepted:    6K
# Total Submissions: 16.4K
# Testcase Example:  '[1,3,2]\n1'
#
#
# There is a garden with N slots. In each slot, there is a flower. The N
# flowers will bloom one by one in N days. In each day, there will be exactly
# one flower blooming and it will be in the status of blooming since then.
#
#
#
# Given an array flowers consists of number from 1 to N. Each number in the
# array represents the place where the flower will open in that day.
#
#
#
# For example, flowers[i] = x means that the unique flower that blooms at day i
# will be at position x, where i and x will be in the range from 1 to N.
#
#
#
# Also given an integer k, you need to output in which day there exists two
# flowers in the status of blooming, and also the number of flowers between
# them is k and these flowers are not blooming.
#
#
#
# If there isn't such day, output -1.
#
#
# Example 1:
#
# Input: 
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become
# blooming.
#
#
#
# Example 2:
#
# Input: 
# flowers: [1,2,3]
# k: 1
# Output: -1
#
#
#
#
# Note:
#
# The given array will be in the range [1, 20000].
#
#
#


class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        if n == 0 or n <= k:
            return -1

        k += 1
        size = (n + k - 1) // k
        bucket = [[float('inf'), float('-inf')] for _ in range(size)]

        for i, pos in enumerate(flowers, 1):
            j = (pos - 1) // k
            if pos < bucket[j][0]:
                bucket[j][0] = pos
                if j > 0 and bucket[j - 1][1] == pos - k:
                    return i
            if pos > bucket[j][1]:
                bucket[j][1] = pos
                if j + 1 < size and bucket[j + 1][0] == pos + k:
                    return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert(sol.kEmptySlots([1, 3, 2], 1) == 2)
    assert(sol.kEmptySlots([1, 2, 3], 1) == -1)
    assert(sol.kEmptySlots([1, 2, 3, 4], 1) == -1)
