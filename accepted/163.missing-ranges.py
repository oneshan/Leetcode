#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges
#
# algorithms
# Medium (23.84%)
# Total Accepted:    32.5K
# Total Submissions: 136.1K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
#
# Given a sorted integer array where the range of elements are in the inclusive
# range [lower, upper], return its missing ranges.
#
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
# "4->49", "51->74", "76->99"].
#
#


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        ans = []
        nums.append(upper + 1)
        s = lower
        for num in nums:
            if s < num:
                if num == s + 1:
                    ans.append(str(s))
                else:
                    ans.append("{0}->{1}".format(s, num - 1))
            s = num + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
    print(sol.findMissingRanges([0, 1, 3, 50, 98], 0, 99))
