"""
Runtime: 2622 ms
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p.replace("*", "")) > len(s):
            return False
        import numpy as np
        table = np.zeros((len(p)+1, len(s)+1), dtype=np.int16)
        table[0][0] = 1
        for j in range(1, len(p)+1):
            table[j][0] = table[j-1][0] and p[j-1]=="*"
            for i in range(1, len(s)+1):
                if p[j-1] != "*":
                    table[j][i] = table[j-1][i-1] and (s[i-1]==p[j-1] or p[j-1]=="?")
                else:
                    table[j][i] = table[j-1][i] or table[j][i-1]

        return bool(table[len(p)][len(s)])


if __name__ == "__main__":
    s = input("s:")
    p = input("p:")
    print(Solution().isMatch(s, p))
