#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string
#
# Easy (58.83%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and returns the string
# reversed.
#
#
# Example:
# Given s = "hello", return "olleh".
#
#


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = list(s)
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            temp[p1], temp[p2] = temp[p2], temp[p1]
            p1 += 1
            p2 -= 1
        return "".join(temp)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.reverseString("hello") == "olleh")
