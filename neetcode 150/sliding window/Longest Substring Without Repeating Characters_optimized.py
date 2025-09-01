class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet= set()
        l = 0
        r = 0
        freq = 0
        while r < len(s):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                freq = max(freq, r-l +1)
                r += 1
            else:
                hashSet.remove(s[l])
                l +=1

        return freq