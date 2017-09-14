#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache
#
# Hard (17.33%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#


class ListNode(object):
    def __init__(self, key, val):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev
        del node

    def insert(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1

        node = self.dict[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.dict:
            node = ListNode(key, value)
            self.insert(node)
            self.size += 1
            if self.size > self.capacity:
                oldest = self.tail.prev
                self.dict.pop(oldest.key)
                self.remove(oldest)
                self.size -= 1
        else:
            node = self.dict[key]
            self.remove(node)
            node.val = value
            self.insert(node)

        self.dict[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
if __name__ == "__main__":
    try:
        from utils.DataStructure import objTest
        obj = LRUCache(2)
        func = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        objTest(obj, func, args)
    except Exception as e:
        print(e)
"""
