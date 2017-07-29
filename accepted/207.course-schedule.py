#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule
#
# Medium (31.66%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '2\n[[1,0]]'
#
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
#
#
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
#
#
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have
# finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have
# finished course 0, and to take course 0 you should also have finished course
# 1. So it is impossible.
#
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
#
#
#
# click to show more hints.
#
# Hints:
#
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be
# impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
# explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.
#
#
#


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        inflow = [0 for i in range(numCourses)]

        for v, u in prerequisites:
            graph[u].append(v)
            inflow[v] += 1

        queue = [v for v in range(numCourses) if inflow[v] == 0]

        while queue:
            u = queue.pop(0)
            for v in graph[u]:
                inflow[v] -= 1
                if inflow[v] == 0:
                    queue.append(v)

        return sum(inflow) == 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(3, [[1, 0]]))
