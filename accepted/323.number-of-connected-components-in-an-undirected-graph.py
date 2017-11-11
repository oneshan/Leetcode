# -*- coding: utf8 -*-
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph
#
# algorithms
# Medium (48.25%)
# Total Accepted:    30.1K
# Total Submissions: 62.4K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
# edge is a pair of nodes), write a function to find the number of connected
# components in an undirected graph.
#
#
#
# ⁠   Example 1:
#
#
# ⁠    0          3
# ⁠    |          |
# ⁠    1 --- 2    4
#
#
# ⁠   Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
#
#
# ⁠   Example 2:
#
#
# ⁠    0           4
# ⁠    |           |
# ⁠    1 --- 2 --- 3
#
#
# ⁠   Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
#
#
#
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges
# are undirected, [0, 1] is the same as [1, 0] and thus will not appear
# together in edges.
#
#
from collections import defaultdict


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = list(range(n))

        def find(parent, x):
            while parent[x] != x:
                x = parent[x]
            return x

        for edge in edges:
            x = find(parent, edge[0])
            y = find(parent, edge[1])
            if x != y:
                n -= 1
                parent[x] = y

        return n

if __name__ == "__main__":
    sol = Solution()
    assert(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2)
    assert(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1)
