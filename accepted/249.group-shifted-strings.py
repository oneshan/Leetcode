# -*- coding: utf8 -*-
#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings
#
# algorithms
# Medium (42.39%)
# Total Accepted:    28.2K
# Total Submissions: 66.5K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
#
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# A solution is:
#
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
#
from collections import defaultdict


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        table = defaultdict(list)
        for string in strings:
            idx = 1
            shift = ord(string[0])
            for ch in string:
                idx = idx * 26 + (ord(ch) + 26 - shift) % 26
            table[idx].append(string)
        return table.values()


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
    print(sol.groupStrings(["aa", "bb", "b"]))
