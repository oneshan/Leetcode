#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream
#
# Hard (25.89%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# Examples: 
# [2,3,4] , the median is 3
# [2,3], the median is (2 + 3) / 2 = 2.5 
#
#
# Design a data structure that supports the following two operations:
#
#
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
#
#
#
# For example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
#
#
# Credits:Special thanks to @Louis1992 for adding this problem and creating all
# test cases.
#
from heapq import heappush, heappushpop


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # max-heap
        self.large = []  # min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.large) == len(self.small):
            return (self.large[0] - self.small[0]) / 2.0
        return float(self.large[0])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert(obj.findMedian() == 1.5)
    obj.addNum(3)
    assert(obj.findMedian() == 2)
