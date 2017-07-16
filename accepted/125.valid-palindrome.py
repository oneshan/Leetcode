#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome
#
# Easy (26.04%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""'
#
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
#
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
#
#
# Note:
# Have you consider that the string might be empty? This is a good question to
# ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
#
#


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j:
            while i < j and (s[i] < '0' or '9' < s[i] < 'a' or 'z' < s[i]):
                i += 1
            while i < j and (s[j] < '0' or '9' < s[j] < 'a' or 'z' < s[j]):
                j -= 1
            if i > j or s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(""))
    print(sol.isPalindrome("ab@a"))
    print(sol.isPalindrome("`l;`` 1o1 ??;l`"))
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    print(sol.isPalindrome("race a car"))
