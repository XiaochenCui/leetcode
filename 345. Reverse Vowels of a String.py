class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        vowels = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'}
        j = len(s) - 1
        i = 0
        s_list = list(s)
        while True:
            while i < len(s) and s_list[i] not in vowels:
                i += 1
            while j >= 0 and s_list[j] not in vowels:
                j -= 1
            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
                continue
            else:
                break
        return ''.join(s_list)


s = Solution
print(s.reverseVowels(s, "OE"))