from itertools import combinations


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r_set = []
        r = []
        for combination in combinations(nums, 3):
            if sum(combination)==0:
                if set(combination) not in r_set:
                    r_set.append(set(combination))
                    r.append(list(combination))
        return r


if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    print r