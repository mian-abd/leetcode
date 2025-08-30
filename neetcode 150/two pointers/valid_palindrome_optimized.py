class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = []
        for ch in s:
            if ch.isalnum():
                new.append(ch)
        l, r = 0, len(new) - 1
        while l < r:
            if new[l] != new[r]:
                return False
            l += 1
            r -= 1
        return True