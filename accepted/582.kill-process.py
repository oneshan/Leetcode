# -*- coding: utf-8 -*-
#
# [582] Kill Process
#
# https://leetcode.com/problems/kill-process
#
# algorithms
# Medium (49.53%)
# Total Accepted:    8.6K
# Total Submissions: 17.4K
# Testcase Example:  '[1,3,10,5]\n[3,0,5,3]\n5'
#
# Given n processes, each process has a unique PID (process id) and its PPID
# (parent process id).
#
# Each process only has one parent process, but may have one or more children
# processes. This is just like a tree structure.  Only one process has PPID
# that is 0, which means this process has no parent process. All the PIDs will
# be distinct positive integers.
#
# We use two list of integers to represent a list of processes, where the first
# list contains PID for each process and the second list contains the
# corresponding PPID.
#
# Now given the two lists, and a PID representing a process you want to kill,
# return a list of PIDs of processes that will be killed in the end. You should
# assume that when a process is killed, all its children processes will be
# killed. No order is required for the final answer.
#
# Example 1:
#
# Input:
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# Output: [5,10]
# Explanation:
# ⁠          3
# ⁠        /   \
# ⁠       1     5
# ⁠            /
# ⁠           10
# Kill 5 will also kill 10.
#
#
#
# Note:
#
# The given kill id is guaranteed to be one of the given PIDs.
# n >= 1.
#
#
#
from collections import defaultdict


class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        table = defaultdict(list)
        for child, parent in zip(pid, ppid):
            table[parent].append(child)

        stack = [kill]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node)
            stack += table[node]
        return ans

if __name__ == "__main__":
    sol = Solution()
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    assert(sol.killProcess(pid, ppid, 5) == [5, 10])
