#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path
#
# Medium (24.97%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '"/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
#
#
# click to show corner cases.
#
# Corner Cases:
#
#
#
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path += '/'

        stack = []
        i = 0
        for j, ch in enumerate(path):
            if ch == '/':
                part, i = path[i:j], j + 1
                if part in ('', '.'):
                    continue
                if part == '..':
                    if stack:
                        stack.pop()
                else:
                    stack += part,
        return '/' + '/'.join(stack)


if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath('/a/./b/../../c/'))
    print(sol.simplifyPath('/home/'))
    print(sol.simplifyPath('/home//foo/'))
    print(sol.simplifyPath('/./'))
    print(sol.simplifyPath('/../'))
    print(sol.simplifyPath('/...'))
