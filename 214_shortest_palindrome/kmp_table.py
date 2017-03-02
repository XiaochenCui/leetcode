"""
Runtime: 75 ms
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = self.constructDFATable(s+"#"+s[::-1])
        flag = table[-1]
        return s[flag:][::-1] + s

    def constructDFATable(self, s):
        """
        :type s: str
        :rtype l: list[int]
        """
        table = [0 for _ in range(len(s))]

        length = 0

        for i in range(1, len(s)):
            if s[length] == s[i]:
                length += 1
                table[i] = length
            else:
                length = table[i-1]

                while length>0 and s[length]!=s[i]:
                    length = table[length-1]

                if s[length] == s[i]:
                    length += 1

                table[i] = length

        return table


if __name__ == "__main__":
    import sys
    print(Solution().shortestPalindrome(sys.argv[1]))
