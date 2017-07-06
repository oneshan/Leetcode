#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval
#
# Hard (27.29%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
#
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as
# [1,2],[3,10],[12,16].
#
#
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
#
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left, right = 0, len(intervals) - 1
        while left <= right and intervals[left].end < newInterval.start:
            left += 1
        while left <= right and intervals[right].start > newInterval.end:
            right -= 1

        # Merge
        if left <= right:
            newInterval.start = min(newInterval.start, intervals[left].start)
            newInterval.end = max(newInterval.end, intervals[right].end)

        return intervals[:left] + [newInterval] + intervals[right + 1:]

if __name__ == "__main__":
    try:
        from utils.Interval import Interval, createInterval, printInterval
        sol = Solution()
        arr = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newInterval = Interval(4, 9)
        intervals = createInterval(arr)
        printInterval(sol.insert(intervals, newInterval))

        arr = [[1, 3], [6, 9]]
        newInterval = Interval(2, 5)
        intervals = createInterval(arr)
        printInterval(sol.insert(intervals, newInterval))

        arr = [[2, 5], [6, 9]]
        newInterval = Interval(1, 3)
        intervals = createInterval(arr)
        printInterval(sol.insert(intervals, newInterval))

    except Exception as e:
        print(e)
        pass
