"""
One pass hash table

Runtime: 482 ms
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numsDict.keys():
                return [numsDict[complement], i]
            if num not in numsDict:
                numsDict[num] = i


if __name__ == '__main__':
    nums = [4, 2, 3]
    target = 6
    print(Solution().twoSum(nums, target))
