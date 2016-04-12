class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bit_dict = {}
        bit_dict[0] = 0
        t = 0
        pow = 1
        for i in range(1, num+1):
            if i == pow:
                pow *= 2
                t = 0
            bit_dict[i] = bit_dict[t]+1
            t += 1
        return bit_dict.values()

s = Solution
answer = s.countBits(s, 5)
print(answer)