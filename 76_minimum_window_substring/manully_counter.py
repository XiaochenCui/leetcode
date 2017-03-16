"""
Runtime: 282 ms
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        import sys
        # dic 记录各字符的需求量
        dic = collections.Counter(t)
        begin = end = 0
        # counter 记录所需的字符总量
        counter = len(t)
        d = sys.maxsize

        for end in range(len(s)):
            if dic[s[end]] > 0:
                counter -= 1
            dic[s[end]] -= 1
            while counter == 0:
                if end-begin < d:
                    head = begin
                    d = end-begin
                if dic[s[begin]] >= 0:
                    counter += 1
                dic[s[begin]] += 1
                begin += 1
        return "" if d==sys.maxsize else s[head:head+d+1]
