"""
Runtime: 55 ms
"""
import re


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        pattern = re.compile(r'^([A-Z]+|[a-z]+|[A-Z][a-z]+)$')
        m = pattern.match(word)
        return True if m else False


if __name__ == '__main__':
    import sys
    print(Solution().detectCapitalUse(sys.argv[1]))
