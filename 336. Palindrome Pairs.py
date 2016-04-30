class Solution(object):
    def palindromePairs(self, words):
        # 0 means the word is not reversed, 1 means the word is reversed
        words, length, result = sorted([(w, 0, i, len(w)) for i, w in enumerate(words)] +
                                       [(w[::-1], 1, i, len(w)) for i, w in enumerate(words)]), len(words) * 2, []
        for i, (word1, rev1, ind1, len1) in enumerate(words):
            for j in range(i + 1, length):
                word2, rev2, ind2, a = words[j]
                if word2.startswith(word1):
                    if ind1 != ind2 and rev1 ^ rev2:
                        rest = word2[len1:]
                        if rest == rest[::-1]: result += ([ind1, ind2],) if rev2 else ([ind2, ind1],)
                else:
                    break
        print(result)
        return result


words = ["abcd", "dcba", "lls", "s", "sssll", "aba"]
s = Solution()
s.palindromePairs(words)
