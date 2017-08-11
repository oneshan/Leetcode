#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii
#
# Medium (51.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing a selected
# element by 1 or decrementing a selected element by 1.
#
# You may assume the array's length is at most 10,000.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 2
#
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
#
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#
#


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        target = nums[len(nums) // 2]
        ans = 0
        for num in nums:
            ans += abs(num - target)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.minMoves2([1, 2, 3]) == 2)
    assert(sol.minMoves2([1, 0, 0, 8, 6]) == 14)
