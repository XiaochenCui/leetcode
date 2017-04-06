"""
Runtime: 42 ms
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)

        if l == 0:
            return 0

        count = [0 for _ in range(l+1)]
        for num in citations:
            if num > l:
                count[l] += 1
            else:
                count[num] += 1
        total = 0
        for i in range(l, -1, -1):
            total += count[i]
            if total >= i:
                return i
