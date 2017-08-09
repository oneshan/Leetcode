#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary
#
# Medium (28.92%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
#
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
#
#
#
#
# ⁠   Example 1:
# ⁠   tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR",
# "SFO"]]
# ⁠   Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
#
#
# ⁠   Example 2:
# ⁠   tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# ⁠   Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# ⁠   Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        table = {}
        for _from, _to in sorted(tickets)[::-1]:
            table.setdefault(_from, [])
            table[_from].append(_to)
        route = []

        def dfs(_from):
            while table.get(_from):
                dfs(table[_from].pop())
            route.append(_from)

        # start from JFK
        dfs("JFK")
        return route[::-1]


if __name__ == "__main__":
    sol = Solution()
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    route = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert(sol.findItinerary(tickets) == route)

    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    route = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert(sol.findItinerary(tickets) == route)

    tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    route = ["JFK", "NRT", "JFK", "KUL"]
    assert(sol.findItinerary(tickets) == route)
