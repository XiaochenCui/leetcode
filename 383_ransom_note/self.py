"""
Too slow

Runtime: 96 ms
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        diff = len(magazine)-len(ransomNote)
        for r in ransomNote:
            for i, m in enumerate(magazine):
                if r==m:
                    magazine = magazine[:i]+"-"+magazine[i+1:]
                    break
        return True if len(magazine.replace("-",""))==diff else False


if __name__ == "__main__":
    ransomNote = input("ransomNote:")
    magazine = input("magazine:")
    print(Solution().canConstruct(ransomNote, magazine))
