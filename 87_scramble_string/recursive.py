"""
Runtime: 95 ms
"""


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        if sorted(s1) != sorted(s2):
            return False

        length = len(s1)
        for i in range(1, length):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[length-i:]) and self.isScramble(s1[i:], s2[:length-i]):
                return True

        return False


if __name__ == "__main__":
    import sys
    print(Solution().isScramble(sys.argv[1], sys.argv[2]))
