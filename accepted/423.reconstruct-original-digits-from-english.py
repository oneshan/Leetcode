#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english
#
# Medium (43.52%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
#
# Note:
#
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
#
#
#
# Example 1:
#
# Input: "owoztneoer"
#
# Output: "012"
#
#
#
# Example 2:
#
# Input: "fviefuro"
#
# Output: "45"
#
#
#


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        ans = [0 for _ in range(10)]
        pair = ((0, "z", "zero"), (2, "w", "two"), (4, "u", "four"), (6, "x", "six"),
                (8, "g", "eight"), (1, "o", "one"), (3, "r", "three"), (5, "f", "five"),
                (7, "s", "seven"), (9, "i", "nine"))

        for ch in s:
            table[ch] = table.get(ch, 0) + 1

        for digit, keyword, engword in pair:
            ans[digit] = table.get(keyword, 0)
            if table.get(keyword):
                for ch in engword:
                    table[ch] -= ans[digit]

        return ''.join([str(i) * ans[i] for i in range(10)])


if __name__ == "__main__":
    sol = Solution()
    assert(sol.originalDigits("owoztneoer") == "012")
    assert(sol.originalDigits("fviefuro") == "45")
