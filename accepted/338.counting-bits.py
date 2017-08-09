#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits
#
# Medium (60.89%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
#
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
#
# Follow up:
#
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount  in c++ or in any other language.
#
#
#
# Credits:Special thanks to @ syedee  for adding this problem and creating all
# test cases.
#


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.countBits(5) == [0, 1, 1, 2, 1, 2])
