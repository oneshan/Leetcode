# -*- coding: utf8 -*-
#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation
#
# algorithms
# Medium (17.13%)
# Total Accepted:    28.7K
# Total Submissions: 167.8K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
# ⁠    1
# b) d|o|g                   --> d1g
#
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#
# ⁠             1
# ⁠    1---5----0
# d) l|ocalizatio|n          --> l10n
#
#
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
#
# Example: 
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
#
#
#


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.table = {}
        self.count = {}

        for word in dictionary:
            abbr = word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word
            if word not in self.table:
                self.table[word] = abbr
                self.count[abbr] = self.count.get(abbr, 0) + 1

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = word[0] + str(len(word) - 2) + word[-1] if len(word) > 2 else word
        if word in self.table:
            return self.count[abbr] == 1
        return abbr not in self.count


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

if __name__ == "__main__":
    dictionary = ["deer", "door", "cake", "card"]
    obj = ValidWordAbbr(dictionary)
    assert(obj.isUnique("deer") is False)
    assert(obj.isUnique("door") is False)
    assert(obj.isUnique("cake") is True)
    assert(obj.isUnique("cane") is False)
