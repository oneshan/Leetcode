#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher
#
# algorithms
# Medium (42.67%)
# Total Accepted:    43.3K
# Total Submissions: 101.5K
# Testcase Example:  '0'
#
#
# There are n bulbs that are initially off. You first turn on all the bulbs.
# Then, you turn off every second bulb. On the third round, you toggle every
# third bulb (turning on if it's off or turning off if it's on). For the ith
# round, you toggle every i bulb. For the nth round, you only toggle the last
# bulb.
#
# Find how many bulbs are on after n rounds.
#
#
#
# Example:
#
# Given n = 3.
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off].
# So you should return 1, because there is only one bulb is on.
#
#


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            sqr = mid * mid
            if sqr == n:
                return mid
            elif sqr > n:
                right = mid - 1
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    sol = Solution()
    assert(sol.bulbSwitch(3) == 1)
    assert(sol.bulbSwitch(9) == 3)
