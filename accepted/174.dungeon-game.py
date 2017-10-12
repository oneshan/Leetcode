#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game
#
# Hard (23.55%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[0]]'
#
#
# The demons had captured the princess (P) and imprisoned her in the
# bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid
# out in a 2D grid. Our valiant knight (K) was initially positioned in the
# top-left room and must fight his way through the dungeon to rescue the
# princess. 
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately. 
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; 
# other rooms are either empty (0's) or contain magic orbs that increase the
# knight's health (positive integers).
# In order to reach the princess as quickly as possible, the knight decides to
# move only rightward or downward in each step. 
#
#
# Write a function to determine the knight's minimum initial health so that he
# is able to rescue the princess.
# For example, given the dungeon below, the initial health of the knight must
# be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
#
# Notes:
#
# The knight's health has no upper bound.
# Any room can contain threats or power-ups, even the first room the knight
# enters and the bottom-right room where the princess is imprisoned.  
#
#
#
# Credits:Special thanks to @stellari for adding this problem and creating all
# test cases.
#


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0

        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[-1][-2] = dp[-2][-1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j], 1)
        return dp[0][0]

if __name__ == "__main__":
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    sol = Solution()
    print(sol.calculateMinimumHP(dungeon))
