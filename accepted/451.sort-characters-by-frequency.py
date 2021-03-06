#
# [451] Sort Characters By Frequency
#
# https://leetcode.com/problems/sort-characters-by-frequency
#
# Medium (50.74%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"tree"'
#
# Given a string, sort it in decreasing order based on the frequency of
# characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
# answer.
#
#
#
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
#
#
#
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
#
#
#
import heapq


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = {}
        for ch in s:
            table[ch] = table.get(ch, 0) + 1

        maxHeap = []
        for ch in table:
            heapq.heappush(maxHeap, (-table[ch], ch))

        ans = ""
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            ans += ch * (count * -1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.frequencySort("aabbbA") == "bbbaaA")
