class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(max(len(version1), len(version2))):
            n1 = int(version1[i]) if len(version1)>i else 0
            n2 = int(version2[i]) if len(version2)>i else 0
            if self.cmp(n1, n2) != 0:
                return self.cmp(n1, n2)
        return 0

    @staticmethod
    def cmp(n1, n2):
        return 1 if n1>n2 else -1 if n1<n2 else 0


if __name__ == '__main__':
    import sys
    print(Solution().compareVersion(sys.argv[1], sys.argv[2]))
