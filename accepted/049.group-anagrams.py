#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams
#
# Medium (33.91%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
# ⁠ ["ate", "eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note: All inputs will be in lower-case.


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                 73, 79, 83, 89, 97, 101]
        chars = dict(zip("abcdefghijklmnopqrstuvwxyz", prime))

        table = {}
        for s in strs:
            key = 1
            for ch in s:
                key *= chars[ch]
            table[key] = table.get(key, []) + [s]

        return [table[key] for key in table]


if __name__ == "__main__":
    sol = Solution()
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(arr))
    arr = ["has", "rod", "tom", "hum", "him", "yon", "met", "dye"]
    print(sol.groupAnagrams(arr))
