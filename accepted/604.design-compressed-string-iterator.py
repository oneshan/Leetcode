#
# [604] Design Compressed String Iterator
#
# https://leetcode.com/problems/design-compressed-string-iterator
#
# algorithms
# Easy (32.40%)
# Total Accepted:    5.2K
# Total Submissions: 15.9K
# Testcase Example:  '["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]\n[["L1e2t1C1o1d1e1"],[],[],[],[],[],[],[],[],[]]'
#
#
# Design and implement a data structure for a compressed string iterator. It
# should support the following operations: next and hasNext.
#
#
#
# The given compressed string will be in the form of each letter followed by a
# positive integer representing the number of this letter existing in the
# original uncompressed string.
#
#
#
# next() - if the original string still has uncompressed characters, return the
# next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#
#
#
# Note:
# Please remember to RESET your class variables declared in StringIterator, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
#
#
#
# Example:
#
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
#
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '
#
#
#


class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.chars = []
        self.count = []
        self.idx = 0
        num = 0
        for ch in compressedString:
            if ch not in '0123456789':
                self.chars.append(ch)
                if num:
                    self.count.append(num)
                num = 0
            else:
                num = num * 10 + int(ch)
        self.count.append(num)
        self.size = len(self.chars)

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        ch = self.chars[self.idx]
        self.count[self.idx] -= 1
        if not self.count[self.idx]:
            self.idx += 1
        return ch

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < self.size


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
if __name__ == "__main__":
    obj = StringIterator("L1e2t1C1o1d1e1")
    while obj.hasNext():
        print(obj.next())
