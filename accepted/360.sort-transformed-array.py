#
# [360] Sort Transformed Array
#
# https://leetcode.com/problems/sort-transformed-array
#
# algorithms
# Medium (44.27%)
# Total Accepted:    13.4K
# Total Submissions: 30.2K
# Testcase Example:  '[-4,-2,2,4]\n1\n3\n5'
#
#
# Given a sorted array of integers nums and integer values a, b and c.  Apply a
# quadratic function of the form f(x) = ax2 + bx + c to each element x in the
# array. 
#
# The returned array must be in sorted order.
#
# Expected time complexity: O(n)
#
# Example:
#
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,
#
# Result: [3, 9, 15, 33]
#
# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
#
# Result: [-23, -5, 1, 7]
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x):
            return a * x * x + b * x + c

        ans = []
        p1, p2 = 0, len(nums) - 1

        while p1 <= p2:
            n1, n2 = f(nums[p1]), f(nums[p2])
            if a > 0:
                if n1 > n2:
                    ans.append(n1)
                    p1 += 1
                else:
                    ans.append(n2)
                    p2 -= 1
            else:
                if n1 > n2:
                    ans.append(n2)
                    p2 -= 1
                else:
                    ans.append(n1)
                    p1 += 1
        return ans if a <= 0 else ans[::-1]

if __name__ == "__main__":
    sol = Solution()
    assert(sol.sortTransformedArray([-4, -2, 2, 4], a=1, b=3, c=5) == [3, 9, 15, 33])
    assert(sol.sortTransformedArray([-4, -2, 2, 4], a=-1, b=3, c=5) == [-23, -5, 1, 7])
    assert(sol.sortTransformedArray([-4, -2, 2, 4], a=0, b=3, c=0) == [-12, -6, 6, 12])
