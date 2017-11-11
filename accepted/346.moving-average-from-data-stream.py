#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream
#
# algorithms
# Easy (59.22%)
# Total Accepted:    29.3K
# Total Submissions: 49.4K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
#
# For example,
#
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#
#
#
from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque()
        self.capacity = size
        self.size = 0
        self.value = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.size == self.capacity:
            self.value -= self.queue.popleft()
        else:
            self.size += 1
        self.queue.append(val)
        self.value += val
        return self.value / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
