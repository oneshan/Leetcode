#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers
#
# Easy (30.37%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
#
#
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
#
#
#
# Note:
#
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
#
#
#


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i]:
                continue
            elif i > 0 and flowerbed[i - 1]:
                continue
            elif i < size - 1 and flowerbed[i + 1]:
                continue
            else:
                n -= 1
                flowerbed[i] = 1
                if not n:
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    
    assert(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1) is True)
    assert(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2) is False)
