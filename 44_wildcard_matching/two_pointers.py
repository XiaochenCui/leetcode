"""
Runtime: 659 ms
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # match 记录匹配 * 的 sIndex 的最大值
        sIndex, pIndex, match, starIndex = 0, 0, 0, -1
        while sIndex < len(s):
            print(sIndex, pIndex, match, starIndex)
            if pIndex < len(p) and (s[sIndex] == p[pIndex] or p[pIndex] == "?"):
                sIndex += 1
                pIndex += 1
            elif pIndex < len(p) and p[pIndex] == "*":
                match = sIndex
                starIndex = pIndex
                pIndex += 1
            elif starIndex != -1:
                match += 1
                sIndex = match
                pIndex = starIndex + 1
            else:
                return False

        while pIndex < len(p) and p[pIndex] == "*":
            pIndex += 1

        return pIndex == len(p)


if __name__ == "__main__":
    s = input("s:")
    p = input("p:")
    print(Solution().isMatch(s, p))
