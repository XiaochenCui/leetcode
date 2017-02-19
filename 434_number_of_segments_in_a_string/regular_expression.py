import re


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        pattern = re.compile(r"\S+")
        return len(pattern.findall(s))


if __name__ == "__main__":
    s = "Hello, my name is John"
    print(Solution().countSegments(s))
