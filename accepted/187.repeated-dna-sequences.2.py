#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences
#
# Medium (31.03%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
#
# For example,
#
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
#
#


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        ans = []

        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        table = {}
        _sum = 0
        for idx, ch in enumerate(s):
            _sum = ((_sum << 2) + mapping[ch]) & 0xFFFFF
            if idx < 9:
                continue
            table[_sum] = table.get(_sum, 0) + 1
            if table[_sum] == 2:
                ans += s[idx - 9:idx + 1],
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
