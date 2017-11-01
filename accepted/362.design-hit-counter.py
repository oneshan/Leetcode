#
# [362] Design Hit Counter
#
# https://leetcode.com/problems/design-hit-counter
#
# algorithms
# Medium (54.33%)
# Total Accepted:    19.1K
# Total Submissions: 35.1K
# Testcase Example:  '["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n[[],[1],[2],[3],[4],[300],[300],[301]]'
#
# Design a hit counter which counts the number of hits received in the past 5
# minutes.
#
# Each function accepts a timestamp parameter (in seconds granularity) and you
# may assume that calls are being made to the system in chronological order
# (ie, the timestamp is monotonically increasing). You may assume that the
# earliest timestamp starts at 1.
#
# It is possible that several hits arrive roughly at the same time.
#
# Example:
#
# HitCounter counter = new HitCounter();
#
# // hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
#
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);
#
#
#
# Follow up:
# What if the number of hits per second could be very large? Does your design
# scale?
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#


class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = [0] * 300
        self.hitcount = [0] * 300

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        bucket = timestamp % 300
        if self.timestamp[bucket] != timestamp:
            self.hitcount[bucket] = 0
            self.timestamp[bucket] = timestamp
        self.hitcount[bucket] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        total = 0
        for i in range(300):
            if timestamp - self.timestamp[i] < 300:
                total += self.hitcount[i]
        return total

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
if __name__ == "__main__":
    obj = HitCounter()
    obj.hit(1)
    obj.hit(2)
    obj.hit(3)
    assert(obj.getHits(4) == 3)
    obj.hit(300)
    assert(obj.getHits(300) == 4)
    assert(obj.getHits(301) == 3)
