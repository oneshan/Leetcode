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

        table = {}
        for i in range(len(s) - 9):
            table[s[i:i + 10]] = table.get(s[i:i + 10], 0) + 1
        return [s for s in table if table[s] > 1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
