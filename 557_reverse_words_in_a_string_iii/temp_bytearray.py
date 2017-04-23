"""
Runtime: 168 ms
"""
from __future__ import print_function
import sys


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = bytearray()
        result = bytearray()
        s += " "
        for c in s:
            if c != " ":
                temp.append(ord(c))
            else:
                temp.reverse()
                result += temp
                result.append(ord(" "))
                temp = bytearray()
        return result[:-1].decode()


if __name__ == "__main__":
    print(Solution().reverseWords(sys.argv[1]))

