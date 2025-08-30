class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for i in s:
            if (ord(i) < 123 and ord(i) > 96) or (ord(i) < 58 and ord(i) > 47) :
                new += i
        if len(new) < 2:
            return True
        le = 0
        right = len(new) -1 
        for i in range(len(new)//2): 
            if ord(new[le]) != ord(new[right]):
                return False
            le +=1
            right -= 1
        return True