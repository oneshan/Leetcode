#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#
# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed
#
# Hard (28.62%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]\n[[],[1],[1],[2],[],[1],[]]'
#
# Design a data structure that supports all following operations in average
# O(1) time.
# Note: Duplicate elements are allowed.
#
#
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The
# probability of each element being returned is linearly related to the number
# of same value the collection contains.
#
#
#
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not
# contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection
# contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains
# [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the
# probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains
# [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
#
#
#
import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.table = {}
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        isDup = val not in self.table
        self.arr += val,
        self.table.setdefault(val, set())
        self.table[val].add(self.size)
        self.size += 1
        return isDup

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.table.get(val):
            return False

        self.size -= 1
        idx = self.table[val].pop()
        if not self.table[val]:
            self.table.pop(val)

        if idx != self.size:
            tmp = self.arr[self.size]
            self.arr[idx] = tmp
            self.table[tmp].remove(self.size)
            self.table[tmp].add(idx)

        self.arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.arr[random.randint(0, self.size - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
if __name__ == "__main__":
    try:
        from utils.DataStructure import objTest
        funs = ["RandomizedCollection", "insert", "insert", "insert", "insert",
                "insert", "insert", "remove", "remove", "remove", "insert", "remove"]
        args = [[], [9], [9], [1], [1], [2], [1], [2], [1], [1], [9], [1]]
        results = [True, False, True, False, True, False, True, True, True, False, True]
        obj = globals()[funs[0]]()
        print(objTest(obj, funs, args) == results)
    except Exception as e:
        print(e)
