#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning
#
# Medium (32.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"aab"'
#
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
#
# Return all possible palindrome partitioning of s.
#
#
# For example, given s = "aab",
#
# Return
#
# [
#   ["aa", "b"],
#   ["a", "a", "b"]
# ]
#
#
#


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []
        self.recur(s, 0, [])
        return self.ans

    def recur(self, s, i, arr):
        if i == len(s):
            self.ans += arr,
        for j in range(i + 1, len(s) + 1):
            if self.isPalindrome(s, i, j - 1):
                self.recur(s, j, arr + [s[i:j]])

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.partition("aab"))
