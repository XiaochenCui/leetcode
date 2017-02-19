"""
Regular expression

Runtime: 62 ms
"""
import re


class Solution(object):

    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ipv4Regex = "((2[0-4]\d|25[0-5]|1\d{2}|[1-9]\d|\d)\.){3}(2[0-4]\d|25[0-5]|1\d{2}|[1-9]\d|\d)"
        ipv6Regex = "(([\da-fA-F]{1,4}):){7}[\da-fA-F]{1,4}"
        if self.exactlyMarch(IP, ipv4Regex):
            return "IPv4"
        elif self.exactlyMarch(IP, ipv6Regex):
            return "IPv6"
        else:
            return "Neither"

    @staticmethod
    def exactlyMarch(text, regex):
        """
        :type text: str
        :type regex: str
        :rtype: Match object
        """
        regex = "^" + regex + "$"
        pattern = re.compile(regex)
        match = pattern.match(text)
        return match


if __name__ == "__main__":
    ip = "172.16.254.100000"
    ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
    print(Solution().validIPAddress(ip))
