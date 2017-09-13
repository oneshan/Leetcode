#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses
#
# Medium (26.91%)
# Total Accepted:   
# Total Submissions:
# Testcase Example:  '"0000"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
#
# For example:
# Given "25525511135",
#
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#
#


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ans = []

        def dfs(idx, remain, ip):
            if remain * 3 < len(s) - idx or remain > len(s) - idx:
                return
            if idx == len(s) and remain == 0:
                self.ans += ip[:-1],
                return
            for i in range(idx, idx + 3):
                if i == len(s) or (i > idx and s[idx] == '0'):
                    break
                if int(s[idx: i + 1]) < 256:
                    dfs(i + 1, remain - 1, ip + s[idx: i + 1] + '.')

        dfs(0, 4, "")
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    assert(sol.restoreIpAddresses("25525511135") == ["255.255.11.135", "255.255.111.35"])
    assert(sol.restoreIpAddresses("010010") == ["0.10.0.10", "0.100.1.0"])
