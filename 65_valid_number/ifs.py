"""
Runtime: 72 ms
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()

        seenE = False
        seenNumber = False
        seenPoint = False
        numberAfterE = True

        for i, c in enumerate(s):
            if ord(c)>=ord("0") and ord(c)<=ord("9"):
                seenNumber = True
                numberAfterE = True
            elif c == ".":
                if seenE or seenPoint:
                    return False
                seenPoint = True
            elif c == "e":
                if seenE or not seenNumber:
                    return False
                seenE = True
                numberAfterE = False
            elif c in ["+", "-"]:
                if i!=0 and s[i-1]!="e":
                    return False
            else:
                return False

        return seenNumber and numberAfterE


if __name__ == "__main__":
    import sys
    print(Solution().isNumber(sys.argv[1]))
