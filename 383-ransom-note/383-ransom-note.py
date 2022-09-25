class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = Counter(magazine)
        if len(ransomNote) > len(magazine):
            return False
        
        for c in ransomNote:
            if freq[c] <= 0:
                return False
            freq[c] -= 1
        
        return True