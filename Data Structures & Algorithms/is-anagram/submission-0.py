class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i in hashS:
                hashS[i] += 1
            else:
                hashS[i] = 1
        
        for j in t:
            if j in hashT:
                hashT[j] += 1
            else:
                hashT[j] = 1
        
        for k in hashS:
            if k not in hashT:
                return False
            if hashS[k] != hashT[k]:
                return False
        
        return True
        
