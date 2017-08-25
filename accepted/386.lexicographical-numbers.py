#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers
#
# Medium (40.81%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '13'
#
#
# Given an integer n, return 1 - n in lexicographical order.
#
#
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
#
#
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
#
#


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.ans = []

        def recur(num):
            num *= 10
            if num > n:
                return
            for i in range(10):
                if num + i > n:
                    return
                self.ans.append(num + i)
                recur(num + i)

        for i in range(1, 10):
            if i > n:
                break
            self.ans.append(i)
            recur(i)

        return self.ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.lexicalOrder(13) == [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])
