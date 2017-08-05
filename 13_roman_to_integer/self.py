import sys
import itertools


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        transfer_table = {None: 0,
                          "I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000}
        su = 0
        for cur, nex in itertools.zip_longest(s, s[1:]):
            if transfer_table[cur] < transfer_table[nex]:
                su -= transfer_table[cur]
            else:
                su += transfer_table[cur]
        return su


if __name__ == "__main__":
    print(Solution().romanToInt(sys.argv[1]))
