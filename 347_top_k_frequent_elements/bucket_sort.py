"""
Runtime: 165 ms
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[len(nums)-freq].append(num)
        return list(itertools.chain(*bucket))[:k]
