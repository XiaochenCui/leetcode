# -*- coding: utf-8 -*-

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='.'):
                s_cur += 1
                p_cur += 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            elif star != -1:
                p_cur = star+1
                match += 1
                s_cur = match
            else:
                return False
        while p_cur<len(p) and p[p_cur]=='*':
            p_cur += 1
        if p_cur == len(p):
            return True
        else:
            return False


if __name__ == '__main__':
    r = Solution.isMatch(Solution(), 'aab', 'c*a*b')
    print r