#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string
#
# Hard (24.41%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '""\n""\n""'
#
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
#
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#
#


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False

        stack = [(0, 0)]
        visit = set()
        while stack:
            p1, p2 = stack.pop()
            if (p1, p2) in visit:
                continue

            visit.add((p1, p2))
            if p1 == n1 and p2 == n2:
                return True
            if p1 < n1 and s1[p1] == s3[p1 + p2]:
                stack.append((p1 + 1, p2))
            if p2 < n2 and s2[p2] == s3[p1 + p2]:
                stack.append((p1, p2 + 1))
        return False 


if __name__ == "__main__":
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    assert(sol.isInterleave(s1, s2, "aadbbcbcac") is True)
    assert(sol.isInterleave(s1, s2, "aadbbbaccc") is False)
    s1 = "cabcccababba"
    s2 = "bbabcbccbc"
    assert(sol.isInterleave(s1, s2, "bbcabacbccbbccccababba") is True)
    s1 = "bcbccabcccbcbbbcbbacaaccccacbaccabaccbabccbabcaabbbccbbbaa"
    s2 = "ccbccaaccabacaabccaaccbabcbbaacacaccaacbacbbccccbac"
    assert(sol.isInterleave(s1, s2, "bccbcccabbccaccaccacbacbacbabbcbccbaaccbbaacbcbaacbacbaccaaccabcaccacaacbacbacccbbabcccccbababcaabcbbcccbbbaa") is False)
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    assert(sol.isInterleave(s1, s2, "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab") is False)
