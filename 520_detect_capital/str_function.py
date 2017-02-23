"""
Using built-in function.

Runtime: 69 ms
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()


if __name__ == "__main__":
    import sys
    print(Solution().detectCapitalUse(sys.argv[1]))
