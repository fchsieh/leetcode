class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        freq = Counter(s)
        
        for c in t:
            if freq[c] == 0:
                return False
            freq[c] -= 1
        
        return True