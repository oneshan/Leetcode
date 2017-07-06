#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game
#
# Medium (29.44%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[2,3,1,1,4]'
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
# Determine if you are able to reach the last index.
#
#
#
# For example:
# A = [2,3,1,1,4], return true.
#
#
# A = [3,2,1,0,4], return false.
#
#


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxLen = 0
        for idx, num in enumerate(nums):
            if idx > maxLen:
                return False
            maxLen = max(maxLen, idx + num)
        return True


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 3, 1, 1, 4]
    print(sol.canJump(arr))

    arr = [3, 2, 1, 0, 4]
    print(sol.canJump(arr))
