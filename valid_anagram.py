class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            curr_char1 = s[i]
            curr_char2 = t[i]
            if curr_char1 in map1:
                map1[curr_char1] += 1
            else:
                map1[curr_char1] = 1
            
            if curr_char2 in map2:
                map2[curr_char2] += 1
            else:
                map2[curr_char2] = 1
        return map1 == map2


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                idx = t.index(char)
                t = t[0:idx] + t[idx+1:]
            else:
                return False
        return len(t)==0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)