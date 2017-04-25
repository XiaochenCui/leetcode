"""
Runtime: 162 ms
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = len(citations)
        left, right = 0, l-1
        while left <= right:
            mid = (right+left)/2
            if citations[mid] >= (l-mid):
                right = mid - 1
            else:
                left = mid + 1
        return l-left
