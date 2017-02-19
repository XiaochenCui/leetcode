class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        if len(nums) <= 3:
            return sum(nums)

        ans = sum(nums[:3])
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = sum([nums[i], nums[j], nums[k]])
                if abs(s - target) < abs(ans - target):
                    ans = s
                if abs(ans - target) == 0:
                    return ans
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return ans


if __name__ == '__main__':
    nums = [-3,-2,-5,3,-4]
    target = -1
    r = Solution.threeSumClosest(Solution(), nums, target)
    print r