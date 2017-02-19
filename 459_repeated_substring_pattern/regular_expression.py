"""
Regular expression

Runtime: 319 ms
"""
import re


class Solution(object):
    def repeatedSubstringPattern(self, string):
        """
        :type str: str
        :rtype: bool
        """
        regex = r"^([a-z]+)\1+$"
        pattern = re.compile(regex)
        m = pattern.match(string)
        return True if m else False


if __name__ == "__main__":
    s = "abcabc"
    print(Solution().repeatedSubstringPattern(s))

