"""
Runtime: 1572 ms
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        for i, num in enumerate(citations[::-1]):
            if num <= i:
                return i
        return len(citations)
