class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_t = []
        new_s = []
        if len(set(s)) == len(set(t)):
            for i in s:
                new_s.append(i)
            for j in t:
                new_t.append(j)
            if sorted(new_s) == sorted(new_t):
                return True
            else:
                return False
        else:
            return False