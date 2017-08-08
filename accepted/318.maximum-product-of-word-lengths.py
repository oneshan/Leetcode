#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths
#
# Medium (43.76%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
#
# ⁠   Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters.
# ⁠   You may assume that each word will contain only lower case letters.
# ⁠   If no such two words exist, return 0.
#
#
#
# ⁠   Example 1:
#
#
# ⁠   Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# ⁠   Return 16
# ⁠   The two words can be "abcw", "xtfn".
#
#
# ⁠   Example 2:
#
#
# ⁠   Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# ⁠   Return 4
# ⁠   The two words can be "ab", "cd".
#
#
# ⁠   Example 3:
#
#
# ⁠   Given ["a", "aa", "aaa", "aaaa"]
# ⁠   Return 0
# ⁠   No such pair of words.    
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = {}
        for idx, word in enumerate(words):
            table[idx] = 0
            for ch in word:
                table[idx] |= (1 << (ord(ch) - 97))  # ord('a') == 97

        ans = 0
        for i in range(len(words)):
            for j in range(i):
                if table[i] & table[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans


if __name__ == "__main__":
    sol = Solution()
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    assert(sol.maxProduct(words) == 16)
    words = ["a", "aa", "aaa", "aaaa"]
    assert(sol.maxProduct(words) == 0)
    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    assert(sol.maxProduct(words) == 4)
