#
# [681] Next Closest Time
#
# https://leetcode.com/problems/next-closest-time
#
# algorithms
# Medium (43.00%)
# Total Accepted:    7.8K
# Total Submissions: 18.2K
# Testcase Example:  '"19:34"'
#
# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can
# be reused.
#
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
# and 59 minutes later.
#
#
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is
# smaller than the input time numerically.
#
#
#


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        self.digits = sorted(list(set(time)))
        self.digits.remove(':')
        self.ans = []
        self.recur("", 0)

        left, right = 0, len(self.ans)
        while left < right:
            mid = (left + right) // 2
            if self.ans[mid] <= time:
                left = mid + 1
            else:
                right = mid
        return self.ans[left] if left < len(self.ans) else self.ans[0]

    def recur(self, string, idx):
        if idx == 4:
            if string[:2] < "24" and string[2:] < "60":
                self.ans.append(string[:2] + ':' + string[2:])
            return
        for d in self.digits:
            self.recur(string + d, idx + 1)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.nextClosestTime("23:59") == "22:22")
    assert(sol.nextClosestTime("19:34") == "19:39")
