#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks
#
# Easy (46.69%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[5,4,3,2,1]'
#
#
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
#
# Example 1:
#
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
#
#
#
# Note:
#
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
#
#
#


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        table = {}
        for rank, num in enumerate(sorted(nums, reverse=True), 1):
            if rank < 4:
                table[num] = ("Gold Medal", "Silver Medal", "Bronze Medal")[rank - 1]
            else:
                table[num] = str(rank)

        return [table[num] for num in nums]


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 4, 3, 2, 1]
    assert(sol.findRelativeRanks(arr) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"])
