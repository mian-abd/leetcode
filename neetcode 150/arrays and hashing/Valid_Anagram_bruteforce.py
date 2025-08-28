#bruteforce
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)
    
        #a = list(s)
        #a = sorted(a)
        #b = list(t)
        #b = sorted(b)
        #return a == b 