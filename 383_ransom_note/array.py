"""
Runtime: 96 ms
"""
from collections import defaultdict


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)
        for c in magazine:
            d[c] += 1
        for c in ransomNote:
            d[c] -= 1
            if d[c] < 0:
                return False
        return True
