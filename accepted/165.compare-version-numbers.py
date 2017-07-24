#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers
#
# Medium (19.88%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"1"\n"0"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise
# return 0.
#
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
# 0.1 < 1.1 < 1.2 < 13.37
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        len1, len2 = len(version1), len(version2)
        p1 = p2 = e1 = e2 = 0
        while p1 < len1 or p2 < len2:
            while e1 < len1 and version1[e1] != '.':
                e1 += 1
            while e2 < len2 and version2[e2] != '.':
                e2 += 1
            v1 = int(version1[p1:e1]) if p1 < e1 else 0
            v2 = int(version2[p2:e2]) if p2 < e2 else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return - 1

            p1 = e1 = e1 + 1
            p2 = e2 = e2 + 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.compareVersion("1.2.1", "1.2"))
    print(sol.compareVersion("1.1.5", "1.1.0.2"))
    print(sol.compareVersion("0.1", "1.1"))
    print(sol.compareVersion("1", "1.0"))
    print(sol.compareVersion("1", "1.1"))
