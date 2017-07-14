#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion
#
# Medium (26.63%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n1'
#
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
#


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        arr = ["" for _ in range(numRows)]
        table = {}
        k = (numRows << 1) - 2
        for i in range(numRows):
            table[i] = table[k - i] = i

        for idx, ch in enumerate(s):
            arr[table[idx % k]] += ch
        return "".join(arr)

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))
