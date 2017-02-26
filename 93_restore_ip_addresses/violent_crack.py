"""
Violent crack use four nested loops.

Runtime: 55 ms
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        for a in range(1,4):
            for b in range(1,4):
                for c in range(1,4):
                    for d in range(1,4):
                        if sum([a,b,c,d]) == len(s):
                            intA = int(s[0:a])
                            intB = int(s[a:a+b])
                            intC = int(s[a+b:a+b+c])
                            intD = int(s[a+b+c:a+b+c+d])
                            if intA<=255 and intB<=255 and intC<=255 and intD<=255 and len(str(intA)) + len(str(intB)) + len(str(intC)) + len(str(intD)) == len(s):
                                results.append(".".join([str(intA),str(intB),str(intC),str(intD)]))
        return results


if __name__ == "__main__":
    import sys
    print(Solution().restoreIpAddresses(sys.argv[1]))

