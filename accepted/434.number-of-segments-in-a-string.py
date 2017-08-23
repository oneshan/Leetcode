#
# [434] Number of Segments in a String
#
# https://leetcode.com/problems/number-of-segments-in-a-string
#
# Easy (36.80%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"Hello, my name is John"'
#
# Count the number of segments in a string, where a segment is defined to be a
# contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5
#
#
#
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, preChar = 0, False
        for ch in s:
            if ch == ' ' and preChar:
                count += 1
            preChar = (ch != ' ')

        if preChar:
            count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    assert(sol.countSegments("Hello, my name is John") == 5)
