"""
DFS

Runtime: 138 ms
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        self.restoreIp(s, results, 0, "", 0)
        return results

    def restoreIp(self, s, results, index, storedPartition, count):
        if count > 4:
            return
        if count == 4 and index == len(s):
            results.append(storedPartition)

        for i in range(1, 4):
            if index+i > len(s):
                break
            tempPartition = s[index:index+i]
            print(tempPartition, count)
            if tempPartition.startswith("0") and i>1 or int(tempPartition)>255:
                continue
            self.restoreIp(s, results, index+i,
                           storedPartition+tempPartition+("." if count<3 else
                                                          ""),
                           count+1)


if __name__ == '__main__':
    import sys
    print(Solution().restoreIpAddresses(sys.argv[1]))
