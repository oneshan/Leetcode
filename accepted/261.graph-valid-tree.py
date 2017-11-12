#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree
#
# algorithms
# Medium (38.00%)
# Total Accepted:    44.1K
# Total Submissions: 116K
# Testcase Example:  '5\n[[0,1],[0,2],[2,3],[2,4]]'
#
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to check whether these edges make
# up a valid tree.
#
#
#
# For example:
#
#
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
#
#
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return
# false.
#
#
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
#
from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        check = [False] * n
        table = defaultdict(list)
        for edge in edges:
            table[edge[0]].append(edge[1])
            table[edge[1]].append(edge[0])

        stack = [0]
        while stack:
            u = stack.pop()
            if check[u]:
                return False
            check[u] = True
            for v in table[u]:
                table[v].remove(u)
                stack.append(v)

        return all(check)

if __name__ == "__main__":
    sol = Solution()
    assert(sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True)
    assert(sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False)
