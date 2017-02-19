"""
Two-pass hash table

Runtime: 672 ms
"""
from collections import defaultdict


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = defaultdict(list)
        for i, v in enumerate(nums):
            numsDict[v].append(i)

        for num in nums:
            complement = target - num
            if complement in numsDict.keys():
                if complement != num:
                    return [numsDict[num][0], numsDict[complement][0]]
                elif len(numsDict[num]) >= 2:
                    return numsDict[num][:2]


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
