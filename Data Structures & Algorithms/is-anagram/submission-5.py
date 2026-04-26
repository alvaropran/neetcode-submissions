class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check if each string is of same length
        if len(s) != len(t):
            return False
        # We need 2 hashmaps for each word/string
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            countT[t[i]] = 1 + countT.get(t[i], 0) 
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
