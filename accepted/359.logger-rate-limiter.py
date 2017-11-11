#
# [359] Logger Rate Limiter
#
# https://leetcode.com/problems/logger-rate-limiter
#
# algorithms
# Easy (59.93%)
# Total Accepted:    20.4K
# Total Submissions: 34K
# Testcase Example:  '["Logger","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage","shouldPrintMessage"]\n[[],[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]'
#
# Design a logger system that receive stream of messages along with its
# timestamps, each message should be printed if and only if it is not printed
# in the last 10 seconds.
#
# Given a message and a timestamp (in seconds granularity), return true if the
# message should be printed in the given timestamp, otherwise returns false.
#
# It is possible that several messages arrive roughly at the same time.
#
# Example:
#
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;
#
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        preTime = self.table.get(message, -10)
        if timestamp - preTime >= 10:
            self.table[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
if __name__ == "__main__":
    obj = Logger()
    assert(obj.shouldPrintMessage(1, "foo") is True)
    assert(obj.shouldPrintMessage(2, "bar") is True)
    assert(obj.shouldPrintMessage(3, "foo") is False)
    assert(obj.shouldPrintMessage(8, "bar") is False)
    assert(obj.shouldPrintMessage(10, "foo") is False)
    assert(obj.shouldPrintMessage(11, "foo") is True)

