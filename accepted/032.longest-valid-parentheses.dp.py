#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses
#
# Hard (22.99%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# For "(()", the longest valid parentheses substring is "()", which has length
# = 2.
#
#
# Another example is ")()())", where the longest valid parentheses substring is
# "()()", which has length = 4.
#
#


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        left = 0
        dp = [0] * len(s)
        for i, ch in enumerate(s):
            if ch == '(':
                left += 1
            elif left > 0:
                left -= 1
                dp[i] = dp[i - 1] + 2
                if i - dp[i] > 0:
                    dp[i] += dp[i - dp[i]]
        return max(dp)


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestValidParentheses('(())'))
    print(sol.longestValidParentheses('())(())'))
    print(sol.longestValidParentheses('()(()'))
    print(sol.longestValidParentheses('()(()))()'))
