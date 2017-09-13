#
# [275] H-Index II
#
# https://leetcode.com/problems/h-index-ii
#
# Medium (34.14%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[]'
#
#
# Follow up for H-Index: What if the citations array is sorted in ascending
# order? Could you optimize your algorithm?
#
#


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if n - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return n - left


if __name__ == "__main__":
    sol = Solution()
    assert(sol.hIndex([0, 1, 3, 5, 6]) == 3)
