#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii
#
# algorithms
# Medium (39.13%)
# Total Accepted:    50.9K
# Total Submissions: 130.1K
# Testcase Example:  '[]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
#
#
# For example,
# Given [[0, 30],[5, 10],[15, 20]],
# return 2.
#
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        points = []
        for interval in intervals:
            points.append((interval.start, 's'))
            points.append((interval.end, 'e'))
        points.sort()

        ans = curr = 0
        for point in points:
            if point[1] == 's':
                curr += 1
                ans = max(ans, curr)
            else:
                curr -= 1

        return ans
