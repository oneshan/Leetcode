#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note
#
# Easy (46.91%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"a"\n"b"'
#
#
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom
# note can be constructed from the magazines ; otherwise, it will return
# false.
#
#
# Each letter in the magazine string can only be used once in your ransom
# note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#
#
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        table = {}
        for ch in magazine:
            table[ch] = table.get(ch, 0) + 1
        for ch in ransomNote:
            if not table.get(ch):
                return False
            table[ch] -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.canConstruct("aa", "ab") is False)
