#
# [657] Judge Route Circle
#
# https://leetcode.com/problems/judge-route-circle
#
# Easy (69.47%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"UD"'
#
#
# Initially, there is a Robot at position (0, 0). Given a sequence of its
# moves, judge if this robot makes a circle, which means it moves back to the
# original place. 
#
#
#
# The move sequence is represented by a string. And each move is represent by a
# character. The valid robot moves are R (Right), L (Left), U (Up) and D
# (down). The output should be true or false representing whether the robot
# makes a circle.
#
#
# Example 1:
#
# Input: "UD"
# Output: true
#
#
#
# Example 2:
#
# Input: "LL"
# Output: false
#
#
#


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = y = 0
        for move in moves:
            if move == "D":
                y += 1
            elif move == "U":
                y -= 1
            elif move == "R":
                x += 1
            else:
                x -= 1
        return x == y == 0


if __name__ == "__main__":
    sol = Solution()
    assert(sol.judgeCircle("LL") is False)
    assert(sol.judgeCircle("DU") is True)
    assert(sol.judgeCircle("LDRRLRUULR") is False)
