#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits
#
# Medium (26.15%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"1432219"\n3'
#
# Given a non-negative integer num represented as a string, remove k digits
# from the number so that the new number is the smallest possible.
#
#
# Note:
#
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.
#
#
#
#
# Example 1:
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
#
#
# Example 2:
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
#
#
# Example 3:
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
#
#
#


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return "0"

        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        if k:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"


if __name__ == "__main__":
    sol = Solution()
    assert(sol.removeKdigits("10200", 1) == "200")
    assert(sol.removeKdigits("1432219", 3) == "1219")
    assert(sol.removeKdigits("112", 1) == "11")
