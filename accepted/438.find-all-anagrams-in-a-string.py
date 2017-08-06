#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string
#
# Easy (33.43%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        n = len(p)

        anagram = [0] * 256
        for ch in p:
            anagram[ord(ch)] += 1

        ans = []
        window = [0] * 256
        for idx, ch in enumerate(s):
            if idx >= n:
                window[ord(s[idx - n])] -= 1
            window[ord(ch)] += 1
            if window == anagram:
                ans += idx - n + 1,
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.findAnagrams("abab", "ab") == [0, 1, 2])
    assert(sol.findAnagrams("cbaebabacd", "abc") == [0, 6])
