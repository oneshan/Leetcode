#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals
#
# Medium (29.61%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.


# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda interval: interval.start)
        ans = [Interval(-1, -1)]
        for elem in intervals:
            if elem.start > ans[-1].end:
                ans += elem,
            else:
                ans[-1].end = max(ans[-1].end, elem.end)
        return ans[1:]

if __name__ == "__main__":
    try:
        from utils.Interval import Interval, createInterval, printInterval
        sol = Solution()
        arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
        intervals = createInterval(arr)
        printInterval(sol.merge(intervals))

        arr = [[1, 4], [0, 4]]
        intervals = createInterval(arr)
        printInterval(sol.merge(intervals))
    except:
        pass
