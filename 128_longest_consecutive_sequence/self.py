class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        d = {}
        for n in nums:
            if n not in d:  # 防止重复计算（nums 中可能有重复元素）
                leftLen = d.get(n-1, 0)
                rightLen = d.get(n+1, 0)
                sumLen = leftLen + rightLen + 1
                d[n] = sumLen
                # 将 sumLen 扩展至边界
                d[n-leftLen] = sumLen
                d[n+rightLen] = sumLen

                res = max(sumLen, res)
        return res
