import re

class Solution(object):
    def __init__(self):
        pass
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num_bin = bin(num)[2:]
        match = re.match(r'1(00)*', num_bin)
        if match:
            if num_bin == match.group():
                return True
        return False

s = Solution()
s.isPowerOfFour(16)
Solution.isPowerOfFour(Solution,16)