#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses
#
# Medium (44.18%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '3'
#
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []

        def dfs(string, left, right):
            if left == right == 0:
                self.ans += string,
                return
            if left > 0:
                dfs(string + "(", left - 1, right)
            if left < right:
                dfs(string + ")", left, right - 1)

        dfs("", n, n)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(0))
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(2))
    print(sol.generateParenthesis(3))

