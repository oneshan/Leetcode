#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string
#
# Easy (38.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
#
# Example 1:
# Given s = "hello", return "holle".
#
#
#
# Example 2:
# Given s = "leetcode", return "leotcede".
#
#
#
# Note:
# The vowels does not include the letter "y".
#
#


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = list(s)
        p1, p2 = 0, len(s) - 1
        while True:
            while p1 < p2 and temp[p1] not in 'aeiouAEIOU':
                p1 += 1
            while p1 < p2 and temp[p2] not in 'aeiouAEIOU':
                p2 -= 1
            if p1 >= p2:
                break
            temp[p1], temp[p2] = temp[p2], temp[p1]
            p1 += 1
            p2 -= 1

        return "".join(temp)


if __name__ == "__main__":
    sol = Solution()
    assert(sol.reverseVowels("hello") == "holle")
    assert(sol.reverseVowels("leetcode") == "leotcede")
