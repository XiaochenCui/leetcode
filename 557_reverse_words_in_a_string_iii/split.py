"""
Runtime: 52 ms
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i[::-1] for i in s.split()])
