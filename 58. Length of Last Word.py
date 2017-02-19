import re


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        pattern = re.compile(r'^\s*([A-Za-z]+\s+)*([A-Za-z]+?)\s*$')
        match = pattern.match(s)
        if match:
            word = match.group(2)
            return len(word)
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLastWord('day')
    print(r)