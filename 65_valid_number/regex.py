"""
Runtime: 125 ms
"""
import re


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = re.match(r"\s*[+-]?(\d+|\d*\.\d+|\d+\.\d*)(e[+-]?\d+)?\s*$", s)
        if m:
            return True
        return False


if __name__ == "__main__":
    import sys
    print(Solution().isNumber(sys.argv[1]))
