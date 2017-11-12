#
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string
#
# algorithms
# Medium (38.67%)
# Total Accepted:    4.7K
# Total Submissions: 12.1K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them.
#
# Example 1:
#
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#
#
#
# Example 2:
#
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
#
#
# Note:
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
#
#
#
class TrieNode(object):
    def __init__(self, idx=0):
        self.child = {}
        self.len = idx
        self.isLeaf = False

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for idx, ch in enumerate(word):
            if ch not in node.child:
                node.child[ch] = TrieNode(idx)
            node = node.child[ch]
        node.isLeaf = True


class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        trie = TrieTree()
        for word in dict:
            trie.insert(word)

        candidates = [trie.root]
        points = []
        for idx, ch in enumerate(s):
            next_round = []
            if ch in trie.root.child:
                next_round.append(trie.root.child[ch])
            for c in candidates:
                if c.isLeaf:
                    points.append((idx - c.len - 1, 0))
                    points.append((idx, 1))
                if ch in c.child:
                    next_round.append(c.child[ch])
            candidates = next_round

        for c in candidates:
            if c.isLeaf:
                points.append((len(s) - c.len - 1, 0))
                points.append((len(s), 1))

        points.sort()
        ans = ""
        i = count = 0
        for p in points:
            if p[1] == 0:
                if count == 0:
                    ans += s[i:p[0]] + '<b>'
                    i = p[0]
                count += 1
            else:
                if count == 1:
                    ans += s[i:p[0]] + '</b>'
                    i = p[0]
                count -= 1
        ans += s[i:]
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "aaabbcc"
    dict = ["aaa", "aab", "bc"]
    assert(sol.addBoldTag(s, dict) == "<b>aaabbc</b>c")

    s = "abcxyz123"
    dict = ["abc", "123"]
    assert(sol.addBoldTag(s, dict) == "<b>abc</b>xyz<b>123</b>")
