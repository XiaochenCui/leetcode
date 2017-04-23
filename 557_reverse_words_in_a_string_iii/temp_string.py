"""
Runtime: 219 ms
"""
from __future__ import print_function
import sys


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = ""
        result = ""
        s += " "
        for c in s:
            if c != " ":
                temp += c
            else:
                result += temp[::-1] + " "
                temp = ""
        return result[:-1]


if __name__ == "__main__":
    print(Solution().reverseWords(sys.argv[1]))
