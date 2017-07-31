#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges
#
# Medium (29.36%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        p1, p2, n = 0, 1, len(nums)
        while p1 < n:
            while p2 < n and nums[p2] == nums[p2 - 1] + 1:
                p2 += 1
            if p2 == p1 + 1:
                ans.append(str(nums[p1]))
            else:
                ans.append("{}->{}".format(nums[p1], nums[p2 - 1]))
            p1, p2 = p2, p2 + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 2, 4, 5, 7]
    assert(sol.summaryRanges(arr) == ["0->2", "4->5", "7"])
