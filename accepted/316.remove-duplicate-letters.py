#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters
#
# Hard (29.24%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"bcabc"'
#
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appear once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
#
#
#
# Example:
#
#
# Given "bcabc"
# Return "abc"
#
#
# Given "cbacdcbc"
# Return "acdb"
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        table = {}
        for ch in s:
            table[ch] = table.get(ch, 0) + 1

        stack = []
        for ch in s:
            table[ch] -= 1
            if ch in stack:
                continue
            while stack and stack[-1] > ch and table[stack[-1]] >= 1:
                stack.pop()
            stack.append(ch)

        return "".join(stack)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.removeDuplicateLetters("bcabc") == "abc")
    assert(sol.removeDuplicateLetters("cbacdcbc") == "acdb")
    assert(sol.removeDuplicateLetters("ccacbaba") == "acb")
    assert(sol.removeDuplicateLetters("edebbed") == "bed")
