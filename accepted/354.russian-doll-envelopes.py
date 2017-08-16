#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes
#
# Hard (31.96%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
#
#
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
#
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
# you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#
#


class Key(list):
    def __lt__(x, y):
        return x[0] < y[0] if x[0] != y[0] else y[1] < x[1]


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=Key)
        lis = []
        for item in envelopes:
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if lis[mid][1] < item[1]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left < len(lis):
                lis[left] = item
            else:
                lis.append(item)
        return len(lis)


if __name__ == "__main__":
    sol = Solution()
    arr = [[5, 4], [6, 4], [6, 7], [2, 3]]
    assert(sol.maxEnvelopes(arr) == 3)
    arr = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
    assert(sol.maxEnvelopes(arr) == 4)
