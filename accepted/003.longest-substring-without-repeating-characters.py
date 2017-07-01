#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters
#
# Medium (24.19%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        ans, start = 0, 0
        for idx, ch in enumerate(s):
            if ch in pos and pos[ch] >= start:
                start = pos[ch] + 1
            ans = max(ans, idx - start + 1)
            pos[ch] = idx
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbb"))
    print(sol.lengthOfLongestSubstring(""))
    print(sol.lengthOfLongestSubstring("abc"))
    print(sol.lengthOfLongestSubstring("a"))
    print(s.lengthOfLongestSubstring("cdd"))
