class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        r = []

        i = 0
        while i < len(nums):
            target = -nums[i]
            front = i + 1
            back = len(nums) - 1

            while front < back:
                if nums[front] + nums[back] < target:
                    front += 1
                elif nums[front] + nums[back] > target:
                    back -= 1
                else:
                    triplet = [nums[i], nums[front], nums[back]]
                    r.append(triplet)
                    while front < len(nums) - 1 and nums[front] == triplet[1]:
                        front += 1
                    while back > i and nums[back] == triplet[2]:
                        back -= 1

            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1

            i += 1

        return r


if __name__ == '__main__':
    r = Solution.threeSum(Solution(), [-1, 0, 1, 2, -1, -4])
    print r