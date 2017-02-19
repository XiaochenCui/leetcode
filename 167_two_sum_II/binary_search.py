"""
Binary search

Runtime: 95 ms
"""


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(numbers):
            left, right = i+1, len(numbers)-1
            complement = target - num
            while left <= right:
                mid = (left+right) // 2
                if numbers[mid] == complement:
                    return [i+1, mid+1]
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    right = mid - 1


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
