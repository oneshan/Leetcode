#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks
#
# Easy (36.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["MyQueue","empty"]\n[[],[]]'
#
#
# Implement the following operations of a queue using stacks.
#
#
# push(x) -- Push element x to the back of queue.
#
#
# pop() -- Removes the element from in front of queue.
#
#
# peek() -- Get the front element.
#
#
# empty() -- Return whether the queue is empty.
#
#
# Notes:
#
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
#
#
#


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                elem = self.stack1.pop()
                self.stack2.append(elem)
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                elem = self.stack1.pop()
                self.stack2.append(elem)
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    assert(obj.pop() == 1)
    assert(obj.peek() == 2)
    assert(obj.empty() is False)
