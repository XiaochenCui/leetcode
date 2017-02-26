"""
Runtime: 252 ms
"""
from collections import OrderedDict


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ""
        d = [1000, 500, 100, 50, 10, 5, 1]
        remainder = num
        while remainder >= 5:
            for n in d:
                if n <= remainder:
                    mod = n
                    break
            quotient, remainder = divmod(remainder, mod)
            s += Solution._intToRoman(quotient, mod)
        s += Solution._intToRoman(remainder, 1)
        d = OrderedDict([("DCCCC", "CM"),
                     ("LXXXX", "XC"),
                     ("VIIII", "IX"),
                     ("CCCC", "CD"),
                     ("XXXX", "XL"),
                     ("IIII", "IV"),
                         ])
        for k, v in d.items():
            s = s.replace(k, v)
        return s

    @staticmethod
    def _intToRoman(num, size):
        d = {1: "I",
             5: "V",
             10: "X",
             50: "L",
             100: "C",
             500: "D",
             1000: "M", }
        return d[size] * num


if __name__ == "__main__":
    import sys
    print(Solution().intToRoman(int(sys.argv[1])))
