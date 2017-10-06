# -*- coding: utf-8 -*-
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii
#
# Hard (23.09%)
# Total Accepted:    
# Total Submissions: 
# Testcase Example:  '["oaan","etae","ihkr","iflv"]\n["oath","pea","eat","rain"]'
#
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
#
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board = 
#
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
#
# Return ["eat","oath"].
#
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
#
# click to show hint.
#
# You would need to optimize your backtracking to pass the larger test. Could
# you stop backtracking earlier?
#
# If the current candidate does not exist in all words' prefix, you could stop
# backtracking immediately. What kind of data structure could answer such query
# efficiently? Does a hash table work? Why or why not? How about a Trie? If you
# would like to learn how to implement a basic trie, please work on this
# problem: Implement Trie (Prefix Tree) first.
#
#


class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.isWord = False


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.isWord = True

    def remove(self, word):
        node = self.root
        stack = []
        for ch in word:
            stack.append((node, ch))
            node = node.child[ch]

        if node.child:
            node.isWord = False
            return

        while stack:
            node, ch = stack.pop()
            del node.child[ch]
            if node.isWord or node.child:
                break


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []

        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        self.trie = TrieTree()
        for word in words:
            self.trie.insert(word)

        self.ans = []
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(i, j, self.trie.root, "", set())
        return self.ans

    def dfs(self, i, j, node, word, visit):
        if (i, j) in visit:
            return False

        ch = self.board[i][j]
        if ch not in node.child:
            return False

        word += ch
        node = node.child[ch]
        if node.isWord:
            self.ans.append(word)
            self.trie.remove(word)

        visit.add((i, j))
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            if 0 <= i + dx < self.m and 0 <= j + dy < self.n:
                self.dfs(i + dx, j + dy, node, word, visit)
        visit.remove((i, j))


if __name__ == "__main__":
    sol = Solution()
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(sol.findWords(board, words))
