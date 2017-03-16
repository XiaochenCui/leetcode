class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i, n in enumerate(nums):
            if i+1!=n:
                return i+1
        return len(nums)+1


if __name__ == "__main__":
    nums = [3,4,-1,1]
    print(Solution().firstMissingPositive(nums))
