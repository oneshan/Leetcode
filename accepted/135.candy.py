#
# [135] Candy
#
# https://leetcode.com/problems/candy
#
# Hard (24.50%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[0]'
#
#
# There are N children standing in a line. Each child is assigned a rating
# value.
#
#
# You are giving candies to these children subjected to the following
# requirements:
#
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
#


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.candy([0]) == 1)
