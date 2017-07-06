#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii
#
# Hard (26.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
#
# Each element in the array represents your maximum jump length at that
# position. 
#
#
# Your goal is to reach the last index in the minimum number of jumps.
#
#
#
# For example:
# Given array A = [2,3,1,1,4]
#
#
# The minimum number of jumps to reach the last index is 2. (Jump 1 step from
# index 0 to 1, then 3 steps to the last index.)
#
#
#
# Note:
# You can assume that you can always reach the last index.
#


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        count, currMax, lastMax = 0, 0, 0
        for idx, num in enumerate(nums):
            if idx > currMax:
                count += 1
                currMax = lastMax
            lastMax = max(lastMax, idx + num)
        return count


if __name__ == "__main__":
    sol = Solution()
    arr = []
    print(sol.jump(arr))

    arr = [2, 3, 1, 1, 4]
    print(sol.jump(arr))

    arr = [2, 1]
    print(sol.jump(arr))
