"""
Runtime: 42 ms
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = path.split("/")
        r = []
        for elem in l:
            if elem not in ["", ".", ".."]:
                r.append(elem)
            elif elem == ".." and len(r) > 0:
                r.pop()

        return "/" + "/".join(r)


if __name__ == "__main__":
    import sys
    print(Solution().simplifyPath(sys.argv[1]))
