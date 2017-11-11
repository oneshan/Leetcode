#
# [358] Rearrange String k Distance Apart
#
# https://leetcode.com/problems/rearrange-string-k-distance-apart
#
# algorithms
# Hard (31.64%)
# Total Accepted:    11.7K
# Total Submissions: 36.8K
# Testcase Example:  '"aabbcc"\n3'
#
#
# Given a non-empty string s and an integer k, rearrange the string such that
# the same characters are at least distance k from each other.
#
#
# All input strings are given in lowercase letters. If it is not possible to
# rearrange the string, return an empty string "".
#
# Example 1:
#
# s = "aabbcc", k = 3
#
# Result: "abcabc"
#
# The same letters are at least distance 3 from each other.
#
#
#
# Example 2:
#
# s = "aaabc", k = 3 
#
# Answer: ""
#
# It is not possible to rearrange the string.
#
#
#
# Example 3:
#
# s = "aaadbbcc", k = 2
#
# Answer: "abacabcd"
#
# Another possible answer is: "abcabcda"
#
# The same letters are at least distance 2 from each other.
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
import heapq


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if not s or not k:
            return s

        table = {}
        heap = []
        ans = [None] * len(s)

        for ch in s:
            table[ch] = table.get(ch, 0) - 1

        for ch, cnt in table.items():
            heapq.heappush(heap, (cnt, ch))

        for i in range(len(s)):
            if i >= k:
                ch = ans[i - k]
                if table[ch]:
                    heapq.heappush(heap, (table[ch], ch))
            if not heap:
                return ""

            cnt, ch = heapq.heappop(heap)
            table[ch] = cnt + 1
            ans[i] = ch

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print(sol.rearrangeString("aaabc", 3))
    print(sol.rearrangeString("aabbcc", 3))
    print(sol.rearrangeString("aaadbbcc", 2))
