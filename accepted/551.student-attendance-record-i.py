#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i
#
# Easy (43.57%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
#
#
#
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
#
# You need to return whether the student could be rewarded according to his
# attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#
#
#

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cA, cL = 0, 0
        for ch in s:
            if ch == 'A':
                cA += 1
            if ch == 'L':
                cL += 1
            else:
                cL = 0
            if cA > 1 or cL > 2:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    assert(sol.checkRecord("PPALLP") is True)
    assert(sol.checkRecord("PPALLL") is False)
