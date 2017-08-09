#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares
#
# Medium (36.34%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '1'
#
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
#
#
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13,
# return 2 because 13 = 4 + 9.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and
# creating all test cases.
#


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square = []
        i = 1
        while i * i <= n:
            square.append(i * i)
            i += 1

        queue = [0]
        visited = {}
        count = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                value = queue.pop(0)
                if value == n:
                    return count
                for i in square:
                    next_value = i + value
                    if next_value > n:
                        break
                    if next_value in visited:
                        continue
                    visited[next_value] = None
                    queue.append(next_value)
            count += 1


if __name__ == "__main__":
    sol = Solution()
    assert(sol.numSquares(12) == 3)
    assert(sol.numSquares(13) == 2)
